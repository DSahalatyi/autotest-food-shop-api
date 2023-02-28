import { Router } from 'express';

import foodController from '../../controllers/food.controller';
import { errorWrapper } from '../../middlewares/error.wrapper';


const router: Router = Router()

// api/food/section/get-all
router.get('/section/get-all', errorWrapper(foodController.getAllFoodSectionList.bind(foodController)))

// api/food/foodItem/getListById
router.post('/item/get-list-by-section', errorWrapper(foodController.getAllFoodItems.bind(foodController)))

//api/food/item/get-list
router.get('/item/get-list', errorWrapper(foodController.getAllFoodItemsById.bind(foodController)))

// api/food-item/:id/find
router.get('/item/:id/find', errorWrapper(foodController.findById.bind(foodController)))

export default router;
