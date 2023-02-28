import mongoose from 'mongoose';
import config from 'config';

async function connectDB () {
    const mongoURL = config.get<string>('mongoURL')
    try {
        await mongoose.connect(mongoURL)
        console.log('Success connection to MongoDB')
    } catch (error) {
        console.error(`Could not connect to MongoDB. Error: ${error}`)
        process.exit(1)
    }
}

export default connectDB
