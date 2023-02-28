import { Request, Response } from 'express'
import { Types } from 'mongoose';

import UserService from '../services/user.service'; 
import PasswordService from '../services/password.service';
import { IUser } from '../models/types/user.type'; 
import { TypedRequestBody } from '../utils/req.body.type';
import { TypedRequestBodyParams } from '../utils/req.body.params.types';


class FoodSectionController {

    constructor (private UserService: UserService,
                 private PasswordService: PasswordService) {}

    async getAll(req: Request, res: Response){
        const docList: IUser[] = await this.UserService.getAll()

        return res.status(200).json({
            status: 200,
            docList
        })
    }

    async delete (req: Request<{id: Types.ObjectId}>, res: Response) {
        const { id } = req.params

        await this.UserService.deleteUserById(id)

        return res.status(200).json({
            message: `${id} has been delete`,
            status: 200
        })
    }

    async findById (req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params
        
        const item: IUser  = await this.UserService.findUserById(id) as IUser
        
        return res.status(200).json({
            status: 200, 
            item 
        })
    }

    async create (req: TypedRequestBody<IUser>, res: Response){
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

    async update (req: TypedRequestBodyParams<{id: Types.ObjectId}, IUser>, res: Response){
        const { id } = req.params

        const {password} = req.body

        const hashPassword = await this.PasswordService.hashPassword(password)
    
        await this.UserService.updateUserById(id, {...req.body, password: hashPassword})
    
        res.status(200).json({
            status: 200,
            message: `${id} has been update`
        })
    }
}

export default new FoodSectionController (new UserService, new PasswordService)
