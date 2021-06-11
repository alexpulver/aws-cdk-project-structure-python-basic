from pathlib import Path

from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigateway
from aws_cdk import core as cdk

from aws_solutions_constructs import aws_apigateway_lambda as apigateway_lambda


class Api(cdk.Construct):
    _RUNTIME_DIR = Path(__file__).resolve().parent.joinpath('runtime')

    def __init__(self, scope: cdk.Construct, id: str) -> None:
        super().__init__(scope, id)

        method_options = apigateway.MethodOptions(authorization_type=apigateway.AuthorizationType.NONE)
        rest_api_props = apigateway.RestApiProps(default_method_options=method_options)
        function_props = _lambda.FunctionProps(
            runtime=_lambda.Runtime.PYTHON_3_7, code=_lambda.Code.from_asset(str(Api._RUNTIME_DIR)),
            handler='app.handler')
        apigateway_lambda.ApiGatewayToLambda(
            self, 'ApiGatewayToLambda', api_gateway_props=rest_api_props,
            lambda_function_props=function_props)
