import swaggerAutogen from 'swagger-autogen'

const outputFile = './swagger_output.json'
const endpointsFiles = [
    './routes/api/admin.route.ts', 
    './routes/api/auth.route.ts', 
    './routes/api/food.item.route.ts', 
    './routes/api/food.section.route.ts', 
    './routes/api/food.route.ts', 
    './routes/api/user.route.ts'
]

swaggerAutogen(outputFile, endpointsFiles)
