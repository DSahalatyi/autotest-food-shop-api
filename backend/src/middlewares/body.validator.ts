import Joi from 'joi'
import { Request, Response, NextFunction } from 'express'

// TODO: 400 status code
export const bodyValidator = (schema: Joi.AnySchema) => 
    async (req: Request, res: Response, next: NextFunction) => {
        const {value, error} = schema.validate(req.body, {abortEarly: false})    
        return error == null ? next() : res.status(409).json(error.details)
    }
       