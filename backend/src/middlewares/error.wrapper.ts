import { Request, Response, NextFunction, json } from "express";

export const errorWrapper = (cntrl: any) => {
    return async (req: Request, res: Response, next: NextFunction) => {
        try { 
            await cntrl(req, res, next)
            res.status(200)
        } catch (error){
            next(error)
        }
    }
} 
