import { Request, Response } from 'express'
import { Types } from 'mongoose';

import FoodSectionService from '../services/food.section.service'; 
import { IFoodSection } from '../models/types/food.section.type'; 
import { TypedRequestBody } from '../utils/req.body.type';
import { TypedRequestBodyParams } from '../utils/req.body.params.types';


class FoodSectionController {

    constructor (private FoodSectionSerive: FoodSectionService) {}

    async getAll(req: Request, res: Response){
        const docList: IFoodSection[] = await this.FoodSectionSerive.getAll()

        return res.status(200).json({
            status: 200,
            docList
        })
    }

    async delete (req: Request<{id: Types.ObjectId}>, res: Response) {
        const { id } = req.params

        await this.FoodSectionSerive.deleteById(id)

        return res.status(200).json({
            message: `${id} has been delete`,
            status: 200
        })
    }

    async findById (req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params

        const item: IFoodSection  = await this.FoodSectionSerive.findById(id) as IFoodSection
        
        return res.status(200).json({ 
            status: 200,
            item 
        })
    }

    async create (req: TypedRequestBody<IFoodSection>, res: Response){
        await this.FoodSectionSerive.create({...req.body})
    
        res.status(201).json({
            status: 201,
            message: `FoodSection has been create`
       })
    }   

    async update (req: TypedRequestBodyParams<{id: Types.ObjectId}, IFoodSection>, res: Response){
        const { id } = req.params

        await this.FoodSectionSerive.updateById(id, {...req.body} )  
    
        res.status(200).json({
            status: 200,
            message: `${id} has been update`
        })
    }

    
}

export default new FoodSectionController (new FoodSectionService)
