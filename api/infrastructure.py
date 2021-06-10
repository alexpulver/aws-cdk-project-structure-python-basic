from pathlib import Path

from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    core as cdk,
)
from aws_solutions_constructs import aws_apigateway_lambda as apigateway_lambda


class Api(cdk.Construct):
    _RUNTIME_DIR = Path(__file__).resolve().parent.joinpath('runtime')

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        apigateway_method_options = apigateway.MethodOptions(authorization_type=apigateway.AuthorizationType.NONE)
        apigateway_rest_api_props = apigateway.RestApiProps(default_method_options=apigateway_method_options)
        lambda_function_props = _lambda.FunctionProps(
            runtime=_lambda.Runtime.PYTHON_3_7, code=_lambda.Code.from_asset(str(Api._RUNTIME_DIR)),
            handler='app.handler')
        apigateway_lambda.ApiGatewayToLambda(
            self, 'ApiGatewayToLambda', api_gateway_props=apigateway_rest_api_props,
            lambda_function_props=lambda_function_props)
