import { DocumentDefinition, Types } from "mongoose";
import config from 'config'

import { IUser } from "../models/types/user.type";
import User from "../models/User.model";

export default class UserService {
    async createUser (data: DocumentDefinition<Omit<IUser, 'is_active'>>) {
        // Allow to create an admin-user only in a debug mode
        const debug: boolean = config.get<boolean>("debug")
        if (debug === false){
            data.is_staff = false
        }
        return await User.create(data)
    }

    async findUserByUsername (username: DocumentDefinition<Pick<IUser, 'username'>>) {
        return await User.findOne(username)
    }

    async findUserByEmail (email: DocumentDefinition<Pick<IUser, 'email'>>) {
        return await User.findOne(email)
    }

    async findUserByPhoneNumber (phone_number: DocumentDefinition<Pick<IUser, 'phone_number'>>){
        return await User.findOne(phone_number)
    }

    async findUserById (id: Types.ObjectId) {
        return await User.findById(id)
    }

    async deleteUserById (id: Types.ObjectId){
        return await User.findByIdAndDelete(id)
    }

    async getAll () {
        return await User.find()
    }

    async updateUserById (id: Types.ObjectId, updateData: DocumentDefinition<IUser>) {
        return await User.findByIdAndUpdate(id, updateData)
    }
}
