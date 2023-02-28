import { Model, model, Schema } from 'mongoose';

import { IFoodSection } from './types/food.section.type'; 

const foodSectionSchema: Schema<IFoodSection> = new Schema({
    name: { 
        type: String, 
        required: true,
        unique: true
    },
    ordering_priority: { 
        type: Number,
        required: true,
        default: 1
    },
    is_available: { 
        type: Boolean, 
        default: false
    }
  }, {
    versionKey: false,
    timestamps: false
  });
  
  const FoodSection: Model<IFoodSection> = model<IFoodSection>('FoodSection', foodSectionSchema)
  
  export default FoodSection;
  