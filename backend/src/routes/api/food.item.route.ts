import { Router } from 'express';

import { errorWrapper } from '../../middlewares/error.wrapper';
import foodItemController from '../../controllers/food.item.controller'; 
import { bodyValidator } from '../../middlewares/body.validator';
import { foodItemSchema} from '../../models/validates/food.item.joi'
import { checkJWT } from '../../middlewares/check.jwt';
import { checkIsStaff } from '../../middlewares/check.is.staff';

const router: Router = Router()

// api/food-item/get-all
router.get('/get-all', checkJWT, checkIsStaff, errorWrapper(foodItemController.getAll.bind(foodItemController)))

// api/food-item/:id/find
router.get('/:id/find', checkJWT, checkIsStaff, errorWrapper(foodItemController.findById.bind(foodItemController)))

// api/food-item/:id/delete
router.get('/:id/delete', checkJWT, checkIsStaff, errorWrapper(foodItemController.delete.bind(foodItemController)))

// api/food-item/create
router.post('/create', checkJWT, checkIsStaff, bodyValidator(foodItemSchema), errorWrapper(foodItemController.create.bind(foodItemController)))

// api/food-item/:id/update
router.post('/:id/update', checkJWT, checkIsStaff, bodyValidator(foodItemSchema), errorWrapper(foodItemController.update.bind(foodItemController)))

export default router;
