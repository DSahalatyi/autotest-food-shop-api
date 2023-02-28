import { Model, model, Schema } from 'mongoose';

import { IOrder, Status } from './types/order.type';

const orderSchema: Schema<IOrder> = new Schema({
    user: {
        type: Schema.Types.ObjectId,
        required: true
    },
    // keys are always strings. You specify the type of values using `of`
    food_items: { 
        type: Map,
        of: Number
    },
    status: {
        type: String,
        required: true,
        enum:  ["new", "processed", "cancelled", "delivered"],
        default: "new"
    },
    payment_method: {
        type: Schema.Types.ObjectId
    }
  }, {
    versionKey: false,
    timestamps: true,
  });
  
  
const Order: Model<IOrder> = model<IOrder>('Order', orderSchema)
  
Order.schema.path('status').validate(function(value: string) {
    return /new|processed|cancelled|delivered/i.test(value);
}, 'Invalid status');

  export default Order;
  