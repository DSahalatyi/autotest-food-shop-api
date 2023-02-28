import express from 'express';
import fileUpload from 'express-fileupload'
import cookieParser  from 'cookie-parser'
import config from 'config'
import cors from 'cors'
import swaggerUi from 'swagger-ui-express'

import swaggerFile from './swagger_output.json'
import connectDB from './utils/connect.db';
import AppRouter from './routes/routes';

const PORT = config.get<number>('port') || 5000

const app = express()
const router = new AppRouter(app)

// Express configuration
app.use(express.json())
app.use(cookieParser())
app.use(express.urlencoded({extended: false}))
app.use(cors({
    credentials: true,
    origin: config.get<string>('clientURL')
}))
app.use(fileUpload({
    createParentPath: true
}))



app.use('/doc', swaggerUi.serve, swaggerUi.setup(swaggerFile))



router.init()

app.listen(PORT, () => {
    console.log(`Server has been start on port ${PORT}...`)
    connectDB()
})
