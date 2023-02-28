import { Application } from 'express';

import authRouter from './api/auth.route'
import adminRouter from './api/admin.route'
import foodRouter from './api/food.route'
import foodSectionRouter from './api/food.section.route'
import foodItemRouter from './api/food.item.route'
import userRouter from './api/user.route'
import orderRouter from './api/order.route'
import paymentMethodRouter from './api/payment.method'

class AppRouter {
    constructor(private app: Application){}
    init() {

        this.app.get('/', (req, res) =>{
            res.status(200)
        })

        this.app.use('/api/auth', authRouter)
        
        this.app.use('/api/admin', adminRouter)

        this.app.use('/api/food', foodRouter)

        this.app.use('/api/food-section', foodSectionRouter)

        this.app.use('/api/food-item', foodItemRouter)

        this.app.use('/api/user', userRouter)

        this.app.use('/api/order', orderRouter)
    
        this.app.use('/api/payment-method', paymentMethodRouter)
    }
}

export default AppRouter;
