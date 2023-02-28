import { Router } from 'express';

import adminController from "../../controllers/admin.controller";
import { errorWrapper } from '../../middlewares/error.wrapper';
import { checkJWT } from '../../middlewares/check.jwt';
import { checkIsStaff } from '../../middlewares/check.is.staff';


const router: Router = Router()

// api/admin/models
router.get('/models', checkJWT, checkIsStaff, errorWrapper(adminController.getModels.bind(adminController)))

// api/admin/:model/keys
router.get('/:model/keys', checkJWT, checkIsStaff, errorWrapper(adminController.getKeys.bind(adminController)))

export default router;
