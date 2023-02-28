import { Model, model, Schema } from 'mongoose';

import { IToken } from './types/token.type';

const tokenSchema: Schema<IToken> = new Schema({
    user_id: { type: Schema.Types.ObjectId, ref: 'User'},
    refresh_token: [ { type: String } ]
  }, {
    versionKey: false,
    timestamps: true
  });
  
const Token: Model<IToken> = model<IToken>('Token', tokenSchema)
  
export default Token;
