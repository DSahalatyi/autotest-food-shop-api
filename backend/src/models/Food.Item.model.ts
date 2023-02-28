import { Model, model, Schema, Types } from 'mongoose';

import { IFoodItem } from './types/food.item.type'; 

const foodItemSchema: Schema<IFoodItem> = new Schema({
    name: { 
        type: String, 
        required: true,
        unique: true
    },
    food_section: { 
        type: Schema.Types.ObjectId, 
        ref: 'FoodSection'},
    ordering_priority: { 
        type: Number,
        required: true,
        default: 1
    },
    is_available: { 
        type: Boolean, 
        default: false
    },
    image: {
        type: String,
        default: ''
    }, 
    price: {
        type: Types.Decimal128,
        required: true
    }
  }, {
    versionKey: false,
    timestamps: false
  });
  
  const FoodItem: Model<IFoodItem> = model<IFoodItem>('FoodItem', foodItemSchema)
  
  export default FoodItem;
  