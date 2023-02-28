import { Request, Response } from 'express'

import ModelService from '../services/model.service';

class AdminController  {
    constructor (private ModelService: ModelService) {}

    async getModels(req: Request, res: Response){
        const _modelList: Array<string> = this.ModelService.getModelNames()
        
        // Doesn't retrieve Token collection due to access restrictions
        const modelList = _modelList.filter(item => item !== 'Token')
        
        return res.status(200).json({
            status: 200,
            modelList
        })
    }

    async getKeys(req: Request<{model: string}>, res: Response){
        const { model } = req.params
        
        let modelKeys: Array<string> = []

        if (model === 'User') {
            modelKeys = this.ModelService.getUserKeys()

        } else if (model === 'FoodSection') {
            modelKeys = this.ModelService.getFoodSectionKeys()

        } else if (model === 'FoodItem') {
            modelKeys = this.ModelService.getFoodItemKeys()

        } else {
            return res.status(404).json({
                status: 404,
                message: 'Not found'
            })
        }

        return res.status(200).json({
            status: 200,
            modelKeys
        })
    }
}

export default new AdminController(new ModelService)
