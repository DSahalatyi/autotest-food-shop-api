import { DocumentDefinition, Types } from "mongoose";

import { IOrder, Status } from '../models/types/order.type'; 
import Order from '../models/Order.model'; 

export default class OrderService {
    async create(data: DocumentDefinition<IOrder>){  
        return await Order.create(data)
    }

    async getAll(){
        return await Order.find()
    }

    async deleteById(id: Types.ObjectId){
        return await Order.findByIdAndDelete(id)
    }

    async findById(id: Types.ObjectId){
        return await Order.findById(id)
    }

    async update(id: Types.ObjectId, updateDate: DocumentDefinition<IOrder>){
        return await Order.findByIdAndUpdate(id, updateDate, { runValidators: true })
    }

    async changeStatusOrder(id: Types.ObjectId, status: DocumentDefinition<Pick<IOrder, "status">>){
        return await Order.findByIdAndUpdate(id, {status: status}, { runValidators: true })
    }
}
