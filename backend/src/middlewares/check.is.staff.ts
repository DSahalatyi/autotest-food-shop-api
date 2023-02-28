import { Request, Response, NextFunction } from 'express';
import jwt, { JwtPayload } from 'jsonwebtoken';
import config from 'config';

export const checkIsStaff = (req: Request, res: Response, next: NextFunction) => {
    const token = req.headers.authorization?.split(" ")[1]
    if (token) {
        const { is_staff } = jwt.verify(token, config.get<string>('accessTokenPrivateKey')) as JwtPayload
        is_staff === true ? next() : res.status(405).json({message: 'Do not has permission'})
    } else {
        return res.status(405).json({msg: 'No token provided.'})
      }
}
