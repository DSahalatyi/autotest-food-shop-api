import Joi from 'joi'
import { Request, Response, NextFunction } from 'express'

export const paramsValidator = (schema: Joi.AnySchema) =>
    async (req: Request, res: Response, next: NextFunction) => 
        await schema.validateAsync(req.params.id) ? next() : res.status(400).json({message: 'Data with such id do not exist'})
        