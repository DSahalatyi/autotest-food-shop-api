import Joi from 'joi';
import { IToken } from '../types/token.type';

export const tokenSchema = Joi.object<IToken>({
    user_id: Joi.string().hex().length(24).required(),
    refresh_token: Joi.array().items({ item: Joi.string() }).length(2)
})
