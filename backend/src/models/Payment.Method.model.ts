import { Model, model, Schema } from 'mongoose';

import { IPaymentMethod } from './types/payment.method.type';

const paymentMethodSchema: Schema<IPaymentMethod> = new Schema({
    name: {
        type: String,
        required: true,
        unique: true
    }
  }, {
    versionKey: false,
    timestamps: false
  });
  
const PaymentMethod: Model<IPaymentMethod> = model<IPaymentMethod>('PaymentMethod', paymentMethodSchema)
  
export default PaymentMethod;
