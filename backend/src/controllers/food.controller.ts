import { Request, Response } from 'express'
import { Types } from 'mongoose';

import FoodSectionService from '../services/food.section.service'; 
import FoodItemService from '../services/food.item.service';

import { IFoodSection } from '../models/types/food.section.type'; 
import { IFoodItem } from '../models/types/food.item.type';

import { TypedRequestBody } from '../utils/req.body.type';
import { TypedRequestQuery } from '../utils/req.query.type'


class FoodController {

    constructor (private FoodSectionSerive: FoodSectionService,
                 private FoodItemService: FoodItemService) {}

    async getAllFoodSectionList(req: Request, res: Response){
        const list: IFoodSection[] = await this.FoodSectionSerive.getAll()

        res.status(200).json({
            status: 200,
            list
        })
    }

    async getAllFoodItemsById(req: TypedRequestQuery <{id: string, count: string, offset: string}>, res: Response) {
        const {id, count, offset} = req.query
        
        const list: any = await this.FoodItemService.getAllFoodItemsByFoodSectionId(id, Number(offset), Number(count))
        if (list === null) res.status(404).json({ status: 200, message: 'Not found'})

        const countDoc = await this.FoodItemService.getCountDocById(id)
        const totalPage = Math.ceil(countDoc / Number(count))
        
        res.status(200).json({
            status: 200,
            list,
            totalPage,
            page: offset
        })
    }

    async getAllFoodItems(req: TypedRequestBody<{id: Types.ObjectId}>, res: Response) {
        const { id } = req.body
        
        const list: any = await this.FoodItemService.getListByFoodSection(id)
        if (list === null) res.status(404).json({ status: 200, message: 'Not found'})
        
        res.status(200).json({
            status: 200,
            list
        })
    }


    
    async findById(req: Request<{id: Types.ObjectId}>, res: Response) {
        const { id } = req.params

        const item: IFoodItem  = await this.FoodItemService.findById(id) as IFoodItem
        
        return res.status(200).json({ 
            status: 200,
            item 
        })
    }

}

export default new FoodController (new FoodSectionService, new FoodItemService)
