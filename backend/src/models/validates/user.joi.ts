import Joi from 'joi';
import { IUser } from '../types/user.type';

export const userSchema = Joi.object<IUser>({
    username: Joi.string().lowercase().min(6).max(20).required().messages({
        'string.base': 'User name should be a type of text',
        'string.empty': 'User name cannot be an empty field',
        'string.min': 'User name should have a minimum length of 6',
        'string.max': 'User name should have a maximum length of 20',
        'string.required': 'User name is a required field'
    }),
    email: Joi.string().email().messages({
        'string.base': 'Email should be a type of text',
        'string.empty': 'Email cannot be an empty field', 
        'string.domain': 'Email shoud have a domain length of 2',
    }),
    password: Joi.string().min(8).max(20).required().messages({
        'string.empty': 'Password cannot be an empty field',
        'string.min': 'Password should have a minimum length of 8',
        'string.max': 'Password should have a maximum length of 20',
        'string.required': 'Password is a required field' 
    }),
    first_name: Joi.string().pattern(/^[A-Z]{1}[a-z]+$/).min(3).max(15).messages({
        'string.pattern.base': 'First name should contain letters only and the first letter should be a capital',
        'string.empty': 'First name cannot be an empty field',
        'string.min': 'First name should have a minimum length of 3',
        'string.max': 'First name should have a maximum length of 15'
    }),
    last_name: Joi.string().pattern(/^[A-Z]{1}[a-z]+$/).min(3).max(20).messages({
        'string.pattern.base': 'Last name should contain letters only and the first letter should be a capital',
        'string.empty': 'Last name cannot be an empty field',
        'string.min': 'Last name should have a minimum length of 3',
        'string.max': 'Last name should have a maximum length of 20'
    }),
    age: Joi.number().greater(14).messages({
        'number.base': 'Age should be a type of number',
        'number.empty': 'Age cannot be an empty field',
        'number.greater': 'Age should be greater than 10',
    }),
    phone_number: Joi.string().pattern(/^\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})$/).messages({
        'string.pattern.base': 'Phone number should contain 10 symbols and start from 0',
        'string.empty': 'Phone number cannot be an empty field',
    }),
    is_staff: Joi.boolean(),
    is_active: Joi.boolean()
})
