import Joi from 'joi';
import { IOrder } from '../types/order.type';

export const orderSchema = Joi.object<IOrder>({
    user: Joi.string().hex().length(24).required(),
    food_items: Joi.required().optional(),
    status: Joi.string().valid('new', 'processed', 'cancelled', 'delivered'),
    payment_method: Joi.string().hex().length(24).required()
})

// address
// originPlace
