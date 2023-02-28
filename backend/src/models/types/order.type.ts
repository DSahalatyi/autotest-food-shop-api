import { Document, Types } from 'mongoose';

export type Status = "new" | "processed" | "cancelled" | "delivered"

export interface IOrder extends Document {
    user: Types.ObjectId;
    food_items: Map<String, Number>,
    status: Status
    payment_method: Types.ObjectId
}
