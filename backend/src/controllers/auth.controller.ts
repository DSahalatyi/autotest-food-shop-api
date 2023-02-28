import { CookieOptions, Request, Response } from 'express';
import config from 'config'

import UserService from '../services/user.service';
import PasswordService from '../services/password.service';
import TokenService from '../services/token.service';

import { TypedRequestBody } from '../utils/req.body.type'
import { IUser } from '../models/types/user.type'
import { Types } from 'mongoose';
import { JwtPayload } from 'jsonwebtoken';

class AuthController {
    constructor(private UserService: UserService, 
                private PasswordService: PasswordService, 
                private TokenService: TokenService) {}

    async register (req: TypedRequestBody<IUser>, res: Response) {
        const {username, email, password, phone_number} = req.body

        const candidateByUsername = await this.UserService.findUserByUsername({username})
        if (candidateByUsername) return res.status(400).json({message: `This username is already in use. Please try different username.`})

        const candidateByEmail = await this.UserService.findUserByEmail({email})
        if (candidateByEmail) return res.status(400).json({message: `This email is already in use. Please try different email.`})

        const candidateByPhoneNumber = await this.UserService.findUserByPhoneNumber({phone_number})
        if (candidateByPhoneNumber) return res.status(400).json({message: `This phone is already in use. Please try different phone.`})

        const hashPassword = await this.PasswordService.hashPassword(password)

        const newUser = await this.UserService.createUser({...req.body, password: hashPassword})
        await newUser.save()

        return res.status(201).json({
            message: 'User has been created',
            status: 201
        })
    } 
    
    async login (req: TypedRequestBody<IUser>, res: Response) {
        const { username, password } = req.body

        const candidate = await this.UserService.findUserByUsername({username})
        if (!candidate) return res.status(400).json({message: 'User with such username does not exist or password is wrong'})

        const isMatchPassword = await this.PasswordService.comparePassword(password, candidate.password)
        if (!isMatchPassword) return res.status(400).json({message: 'User with such username does not exist or password is wrong'})

        if (candidate.is_active === false) res.status(400).json({message: 'User with such username does not have an access to content'})

        const payload = {
            _id: candidate._id as Types.ObjectId,
            username: candidate.username,
            is_staff: candidate.is_staff
        }
        
        const {accessToken, refreshToken} = this.TokenService.generateToken(payload)
        
        const tokenCandidate = await this.TokenService.findTokenByUserId(payload._id)
        
        if (tokenCandidate ) {
            if (tokenCandidate.refresh_token.length > 1) {
                await this.TokenService.popTokenByUserId(tokenCandidate.user_id)
            } 
            await this.TokenService.pushTokenByUserId(tokenCandidate.user_id, refreshToken)
        } else {
            const newtoken = await this.TokenService.createToken(candidate._id)
            await newtoken.save()
            await this.TokenService.pushTokenByUserId(newtoken.user_id, refreshToken)
        }

        const cookieOptions : CookieOptions = {
            expires: new Date (
                Date.now() + config.get<number>('refreshTokenExpiresInDays') * 24 * 60 * 60 * 1000
            ),
            maxAge: config.get<number>('refreshTokenExpiresInDays') * 24 * 60 * 60 * 1000,
            httpOnly: true
        }

        res.cookie('refresh_token', refreshToken, cookieOptions)

        return res.status(200).json({
            message: 'Success login',
            status: 200,
            username: candidate.username,
            is_staff: candidate.is_staff,
            id: candidate._id,
            accessToken,
            refreshToken
        })
    }

    async logout (req: Request, res: Response) {
        const { refresh_token } = req.cookies
        if (!refresh_token) return res.status(403).json({
            message: 'The client does not have access rights to the content'
        })

        const { _id } = this.TokenService.veriftyRefreshToken(refresh_token) as JwtPayload

        await this.TokenService.findAndPullToken(_id, refresh_token)

        res.clearCookie('refresh_token')

        return res.status(200).json({
            message: 'success logout',
            status: 200
        })
    }

    async refresh (req: Request, res: Response) {

        const { refresh_token } = req.cookies
        if (refresh_token === null) return res.status(405).json('No token provided') 
            
        const { _id } = this.TokenService.veriftyRefreshToken(refresh_token) as JwtPayload
        if (!_id) return res.status(403).json({message: 'Forbidden decoded'})
        
        const token = await this.TokenService.findTokenByUserId(_id)
        if (!token) return res.status(403).json({message: 'Forbidden session'})
            
        const user = await this.UserService.findUserById(_id)
        if (!user) return res.status(403).json({message: 'Forbidden user'})
    
        await this.TokenService.findAndPullToken(_id, refresh_token)
    
        res.clearCookie('refresh_token')
    
        const payload = {
            _id: user._id,
            username: user.username,
            is_staff: user.is_staff
        }
    
        const {accessToken, refreshToken} = this.TokenService.generateToken(payload)
            
        await this.TokenService.pushTokenByUserId(payload._id, refreshToken)
    
        const cookieOptions : CookieOptions = {
            expires: new Date (
                Date.now() + config.get<number>('refreshTokenExpiresInDays') * 24 * 60 * 60 * 1000
            ),
            maxAge: config.get<number>('refreshTokenExpiresInDays') * 24 * 60 * 60 * 1000,
            httpOnly: true
        }
    
        res.cookie('refresh_token', refreshToken, cookieOptions)
    
        return res.status(200).json({
            message: 'Success refresh',
            status: 200,
            accessToken,
            refreshToken,
            is_staff: user.is_staff,
            username: user.username,
            id: user._id
        })
    }
}

export default new AuthController(new UserService, new PasswordService, new TokenService)
