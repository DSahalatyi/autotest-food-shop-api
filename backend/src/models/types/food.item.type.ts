import { Document, Types } from 'mongoose';

export interface IFoodItem extends Document {
    name: String;
    food_section: Types.ObjectId;
    ordering_priority: Number;
    is_available?: Boolean;
    image?: String;
    price: Types.Decimal128;
}

export interface IFoodItemDto extends Document {
    name: String;
    food_section: Types.ObjectId;
    ordering_priority: Number;
    is_available?: Boolean;
    image?: String;
    price: Types.Decimal128;
    file?: any
}
