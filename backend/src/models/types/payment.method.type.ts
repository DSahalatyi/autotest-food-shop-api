import { Document } from 'mongoose';

export interface IPaymentMethod extends Document {
    name: string;
}
