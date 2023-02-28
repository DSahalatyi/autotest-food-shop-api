import { DocumentDefinition, Types } from "mongoose";

import { IFoodSection } from '../models/types/food.section.type'; 
import FoodSection from '../models/Food.Section.model'; 

export default class FoodSectionService {
    async create(data: DocumentDefinition<IFoodSection>) {
        return await FoodSection.create(data)
    }

    async deleteById(id: Types.ObjectId) {
        return await FoodSection.findByIdAndDelete(id)
    }

    async findById(id: Types.ObjectId) {
        return await FoodSection.findById(id)
    }

    async updateById(id: Types.ObjectId, updateData: DocumentDefinition<IFoodSection>) {
        return await FoodSection.findByIdAndUpdate(id, updateData)
    }

    async getAll(){
        return await FoodSection.find()
    }

    async findByName(name: DocumentDefinition<Pick<IFoodSection, "name">>) {
        return await FoodSection.findOne(name)
    }
}
