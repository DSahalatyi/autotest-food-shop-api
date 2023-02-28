import { Request, Response } from 'express';
import { Types } from 'mongoose';

import PaymentMethodService from '../services/payment.method.service';

import { IPaymentMethod} from '../models/types/payment.method.type'; 

import { TypedRequestBody } from '../utils/req.body.type';
import { TypedRequestBodyParams } from '../utils/req.body.params.types';


class PaymentMethodController {

    constructor (private PaymentMethodService: PaymentMethodService) {}
    
    async getAll(req: Request, res: Response){
        const docList: IPaymentMethod[] = await this.PaymentMethodService.getAll()

        return res.status(200).json({
            status: 200,
            docList
        })
    }
    
    async delete(req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params

        const payment = await this.PaymentMethodService.findById(id)
        if (!payment) return res.status(404).json({ message: `Payment method ${id} do not exist. Please, try again.` })
    
        await this.PaymentMethodService.deleteById(id)

        return res.status(200).json({
            message: `${id} has been delete`,
            status: 200
        })
    }

    async findById(req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params

        const item: IPaymentMethod = await this.PaymentMethodService.findById(id) as IPaymentMethod
        
        return res.status(200).json({ 
            status: 200,
            item 
        })
    }

    async create(req: TypedRequestBody<IPaymentMethod>, res: Response){
        const { name } = req.body
        
        const payment = await this.PaymentMethodService.findByName({name})
        if (payment) return res.status(400).json({ message: `Payment method ${name} has already exist`})
    
        await this.PaymentMethodService.create({name})
        res.status(201).json({
            status: 201,
            message: 'Created'
        })
    }

    async update(req: TypedRequestBodyParams<{id: Types.ObjectId}, IPaymentMethod>, res: Response){
        const { id } = req.params
        const { name } = req.body
    
        const payment = await this.PaymentMethodService.findById(id)
        if (!payment) return res.status(404).json({ message: `Payment method ${id} do not exist. Please, try again!`})
       
        const nameCandidate = await this.PaymentMethodService.findByName({name})
        if (nameCandidate) return res.status(400).json({ message: `Payment method ${name} has already exist`})
    
        await this.PaymentMethodService.update(id, {name})
        return res.status(200).json({
            status: 200,
            message: `Payment method ${id} has been change`
        })
    }

}

export default new PaymentMethodController (new PaymentMethodService)
