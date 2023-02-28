import Joi from 'joi';
import { IFoodItemDto } from '../types/food.item.type'; 

export const foodItemSchema = Joi.object<IFoodItemDto>({
    name: Joi.string().min(4).max(40).required().messages({
        'string.base': 'Name name should be a type of text',
        'string.empty': 'Name name cannot be an empty field',
        'string.min': 'Name should have a minimum length of 4',
        'string.max': 'Name should have a maximum length of 40',
        'string.required': 'Name is a required field'
    }),
    ordering_priority: Joi.number().greater(0).required().messages({
        'number.base': 'Ordering priority should be a type of number',
        'number.empty': 'Ordering priority cannot be an empty field',
        'number.greater': 'Ordering priority should be greater than 0',
    }),
    is_available: Joi.boolean(),
    price: Joi.required(),
    food_section: Joi.string().hex().length(24).required(),
    image: Joi.string().required(),
    file: Joi.binary()
})
