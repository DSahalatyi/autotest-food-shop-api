import mongoose, { Document, Model, Schema } from 'mongoose';

import User from "../models/User.model";
import Token from '../models/Token.model';
import FoodSection from '../models/Food.Section.model'; 
import FoodItem from '../models/Food.Item.model';

class ModelService {
    getModelNames () {
        return mongoose.modelNames()
    }

    getUserKeys () {
        return Object.keys(User.schema.paths)
    }

    getTokenKeys () {
        return Object.keys(Token.schema.paths)
    }

    getFoodSectionKeys () {
        return Object.keys(FoodSection.schema.paths)
    }

    getFoodItemKeys () {
        return Object.keys(FoodItem.schema.paths)
    }
}

export default ModelService
