import { DocumentDefinition, Types } from "mongoose";

import { IPaymentMethod } from '../models/types/payment.method.type'; 
import PaymentMethod from '../models/Payment.Method.model'; 

export default class PaymentMethodService {
    async create(data: DocumentDefinition<IPaymentMethod>){  
        return await PaymentMethod.create(data)
    }

    async getAll(){
        return await PaymentMethod.find()
    }

    async deleteById(id: Types.ObjectId){
        return await PaymentMethod.findByIdAndDelete(id)
    }

    async findById(id: Types.ObjectId) {
        return await PaymentMethod.findById(id)
    }

    async update(id: Types.ObjectId, updateData: DocumentDefinition<Pick<IPaymentMethod, 'name'>>){
        return await PaymentMethod.findByIdAndUpdate(id, updateData)
    }

    async findByName(name: DocumentDefinition<Pick<IPaymentMethod, 'name'>>){
        return await PaymentMethod.findOne(name)
    }
}
