import { Router } from 'express';

import { errorWrapper } from '../../middlewares/error.wrapper';
import paymentMethodController from '../../controllers/payment.method.controller'
import { bodyValidator } from '../../middlewares/body.validator';
import { paymentMethodSchema } from '../../models/validates/payment.method.joi';
import { checkJWT } from '../../middlewares/check.jwt';
import { checkIsStaff } from '../../middlewares/check.is.staff';


const router: Router = Router()

// api/payment-method/get-all
router.get('/get-all', checkJWT, errorWrapper(paymentMethodController.getAll.bind(paymentMethodController)))

// api/payment-method/:id/find
router.get('/:id/find', checkJWT, checkIsStaff, errorWrapper(paymentMethodController.findById.bind(paymentMethodController)))

// api/payment-method/:id/delete
router.get('/:id/delete', checkJWT, checkIsStaff, errorWrapper(paymentMethodController.delete.bind(paymentMethodController)))

// api/payment-method/create
router.post('/create', checkJWT, checkIsStaff, bodyValidator(paymentMethodSchema), errorWrapper(paymentMethodController.create.bind(paymentMethodController)))

// api/payment-method/:id/update
router.post('/:id/update', checkJWT, checkIsStaff, bodyValidator(paymentMethodSchema), errorWrapper(paymentMethodController.update.bind(paymentMethodController)))

export default router;
