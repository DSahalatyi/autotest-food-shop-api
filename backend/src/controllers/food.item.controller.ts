import { Request, Response } from 'express'
import { DocumentDefinition, Types } from 'mongoose';
import fileUpload, {  UploadedFile } from 'express-fileupload';
import fs from 'fs'

import FoodItemService from '../services/food.item.service';
import { IFoodItem } from '../models/types/food.item.type';
import { TypedRequestBodyParams } from '../utils/req.body.params.types';

class FoodSectionController {

    constructor (private FoodItemService: FoodItemService) {}

    async getAll(req: Request, res: Response){
        const docList: IFoodItem[] = await this.FoodItemService.getAll()
    
        return res.status(200).json({ 
            status: 200, 
            docList
        })
    }

    async delete (req: Request<{id: Types.ObjectId}>, res: Response) {
        const { id } = req.params

        const foodItemData = await this.FoodItemService.findById(id)
        if(!foodItemData) return res.status(404).json({message: `Food item with such id ${id} - not found`})

        fs.stat(`${__dirname}\\..\\..\\..\\food-shop-frontend\\public\\images\\${foodItemData.image}`, err => {
        // check file before delete whether it exist or not
            if (err) {
                return res.status(404).json({message: 'File name or path is incorrect'})
            }
        })
        
        await this.FoodItemService.deleteById(id)
        
        fs.unlink(`${__dirname}\\..\\..\\..\\food-shop-frontend\\public\\images\\${foodItemData.image}`, err => {
            if (err) {
                return res.status(500).json(err)
            }
        })

        return res.status(200).json({
            message: `${id} has been deleted`,
            status: 200
        })
    }

    async findById (req: Request<{id: Types.ObjectId}>, res: Response){
        const { id } = req.params

        const item: IFoodItem  = await this.FoodItemService.findById(id) as IFoodItem
        
        return res.status(200).json({ 
            status: 200,
            item 
        })
       
    }

    async create (req: Request, res: Response){
        if (!req.files) return res.status(400).json({
            status: 400,
            message: "No file uploaded"
        })
        
        const { file } = req.files
        const imageFile: UploadedFile = file as UploadedFile

        imageFile.name = encodeURI(imageFile.name.replace(/\s/g, ''))
    
        await this.FoodItemService.create({...req.body, image: imageFile.name})

        imageFile.mv(`${__dirname}\\..\\..\\..\\food-shop-frontend\\public\\images\\${imageFile.name}`, err => {
            if (err) {
                return res.status(500).json(err)
            }
        })

        return res.status(201).json({
            status: 201,
            message: `FoodItem has been created`
        })
    }   

    async update (req: Request, res: Response){
        const { id } = req.params
        const { image } = req.body as DocumentDefinition<Pick<IFoodItem, 'image'>>
        
        const { food_section } = req.body as DocumentDefinition<Pick<IFoodItem, 'food_section'>>
        
        if (req.files) {
            const { file } = req?.files
            const imageFile: UploadedFile = file as UploadedFile

            imageFile.name = encodeURI(imageFile.name.replace(/\s/g, ''))

            fs.stat(`${__dirname}\\..\\..\\..\\food-shop-frontend\\public\\images\\${image}`, err => {
                if (err) {
                    return res.status(404).json({message: 'File name or path is incorrect'})
                }
            })

            fs.unlink(`${__dirname}\\..\\..\\..\\food-shop-frontend\\public\\images\\${image}`, err => {
                if (err) {
                    return res.status(500).json(err)
                }
            })

            imageFile.mv(`${__dirname}\\..\\..\\..\\food-shop-frontend\\public\\images\\${imageFile.name}`, err => {
                if (err) {
                    return res.status(500).json(err)
                }
            })
            
            await this.FoodItemService.updateById(id, {...req.body, image: imageFile.name, food_section: food_section as Types.ObjectId})
            
            return res.status(200).json({
                status: 200,
                message: `${id} has been updated`
            })
        }
    
        await this.FoodItemService.updateById(id, {...req.body})  
    
        return res.status(200).json({
            status: 200,
            message: `${id} has been updated`
        })

    }  
}

export default new FoodSectionController (new FoodItemService)
