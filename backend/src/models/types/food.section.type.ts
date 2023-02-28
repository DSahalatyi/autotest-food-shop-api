import { Document } from 'mongoose';

export interface IFoodSection extends Document {
    name: String;
    ordering_priority: Number;
    is_available?: Boolean;
}
