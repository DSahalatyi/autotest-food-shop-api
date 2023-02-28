import { Router } from 'express';

import orderController from '../../controllers/order.controller';
import { errorWrapper } from '../../middlewares/error.wrapper';
import { bodyValidator } from '../../middlewares/body.validator';
import { orderSchema } from '../../models/validates/order.joi';
import { checkJWT } from '../../middlewares/check.jwt';
import { checkIsStaff } from '../../middlewares/check.is.staff';

const router: Router = Router()

// api/order/get-all
router.get('/get-all', checkJWT, checkIsStaff, errorWrapper(orderController.getAll.bind(orderController)))

// api/order/:id/find
router.get('/:id/find', checkJWT, errorWrapper(orderController.findById.bind(orderController)))

// api/order/:id/delete
router.get('/:id/delete', checkJWT, checkIsStaff, errorWrapper(orderController.delete.bind(orderController)))

// api/order/create
router.post('/create', checkJWT, bodyValidator(orderSchema), errorWrapper(orderController.create.bind(orderController)))

// api/order/:id/update
router.post('/:id/update', checkJWT, checkIsStaff, errorWrapper(orderController.update.bind(orderController)))

// api/order/:id/change-status
router.post('/:id/change-status', checkJWT, checkIsStaff, errorWrapper(orderController.chachgeStatusOrder.bind(orderController)))

export default router;
