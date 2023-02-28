export interface TypedRequestBodyParams<Params, ReqBody> extends Express.Request {
    body: ReqBody,
    params: Params
}
