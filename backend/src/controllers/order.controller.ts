import { Request, Response } from 'express';
import { DocumentDefinition, Types } from 'mongoose';

import OrderService from '../services/order.service';
import UserService from '../services/user.service';
import PaymentMethodService from '../services/payment.method.service';

import { IOrder} from '../models/types/order.type'; 

import { TypedRequestBody } from '../utils/req.body.type';
import { TypedRequestBodyParams } from '../utils/req.body.params.types';


class OrderController {

    constructor (private OrderSerive: OrderService,
                 private UserService: UserService,
                 private PaymentMethodService: PaymentMethodService) {}
    
    async getAll(req: Request, res: Response){
        const docList: IOrder[] = await this.OrderSerive.getAll()
        
        return res.status(200).json({
            status: 200,
            docList
        })
    }
    
    async delete(req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params

        const order = await this.OrderSerive.findById(id)
        if (!order) return res.status(404).json({ message: `Order ${id} do not exist. Please, try again.` })

        await this.OrderSerive.deleteById(id)

        return res.status(200).json({
            message: `${id} has been deleted`,
            status: 200
        })
    }

    async findById(req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params

        const item: IOrder  = await this.OrderSerive.findById(id) as IOrder
        
        return res.status(200).json({ 
            status: 200,
            item 
        })
    }

    async create(req: TypedRequestBody<IOrder>, res: Response){
        const { user, payment_method } = req.body

        const userData = await this.UserService.findUserById(user)        
        if (!userData) return res.status(404).json({ message: 'User with such id do not exist. Try again' })

        const paymentData = await this.PaymentMethodService.findById(payment_method)
        if (!paymentData) return res.status(404).json({ message: 'Payment method with such id do not exist. Try again' })

        const order = await this.OrderSerive.create({...req.body})
        
        return res.status(201).json({
            status: 201,
            message: 'Created',
            id: order._id
        })
    }

    async update(req: TypedRequestBodyParams<{id: Types.ObjectId}, IOrder>, res: Response){
        const { id } = req.params
        const { user, payment_method } = req.body

        const order = await this.OrderSerive.findById(id)
        if (!order) return res.status(404).json({ message: `Order ${id} do not exist. Please, try again!`})
        
        const userData = await this.UserService.findUserById(user)        
        if (!userData) return res.status(404).json({ message: 'User with such id do not exist. Please, try again' })

        const paymentData = await this.PaymentMethodService.findById(payment_method)
        if (!paymentData) return res.status(404).json({ message: 'Payment method with such id do not exist. Please, try again' })

        await this.OrderSerive.update(id, {...req.body}).catch(error =>
            res.status(404).json({ message: `Order status can not be equal to ${error.errors.status.value}`}))

        return res.status(200).json({
            status: 200,
            message: `${id} order has been updated`
        })
    }

    async chachgeStatusOrder (req: TypedRequestBodyParams<{id: Types.ObjectId}, {status: DocumentDefinition<Pick<IOrder, "status">>}>, res: Response) {
        const { id } = req.params
        const { status } = req.body

        const order = await this.OrderSerive.findById(id)
        if (!order) return res.status(404).json({ message: `Order ${id} do not exist. Please, try again!`})
       
        await this.OrderSerive.changeStatusOrder(id, status).catch(error =>
        res.status(404).json({ message: `Order status can not be equal to ${error.errors.status.value}`}))
        
        return res.status(200).json({
            status: 200,
            message: `${id} order has been changed on status ${status}`
        })
    }
}

export default new OrderController (new OrderService, new UserService, new PaymentMethodService)
