import Joi from 'joi';
import { IPaymentMethod } from '../types/payment.method.type';

export const paymentMethodSchema = Joi.object<IPaymentMethod>({
    name: Joi.string().min(4).max(20).required().messages({
        'string.base': 'Name name should be a type of text',
        'string.empty': 'Name name cannot be an empty field',
        'string.min': 'Name should have a minimum length of 4',
        'string.max': 'Name should have a maximum length of 20',
        'string.required': 'Name is a required field'
    })
})
