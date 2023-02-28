import { Router } from 'express';

import { bodyValidator } from '../../middlewares/body.validator';
import { userSchema } from '../../models/validates/user.joi';
import { errorWrapper } from '../../middlewares/error.wrapper';
import authController from '../../controllers/auth.controller';
import { checkJWT } from '../../middlewares/check.jwt';

const router: Router = Router()

// api/auth/register
router.post('/register', bodyValidator(userSchema), errorWrapper(authController.register.bind(authController)))

// api/auth/login
router.post('/login', bodyValidator(userSchema), errorWrapper(authController.login.bind(authController)))

// api/auth/logout
router.post('/logout', errorWrapper(authController.logout.bind(authController)))

// api/auth/refresh
router.get('/refresh', errorWrapper(authController.refresh.bind(authController)))

export default router;
