import pathlib
from typing import cast

from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_lambda as lambda_
from aws_cdk import core as cdk
from aws_solutions_constructs import aws_apigateway_lambda as apigateway_lambda


class API(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id_: str) -> None:
        super().__init__(scope, id_)

        method_options = apigateway.MethodOptions(
            authorization_type=apigateway.AuthorizationType.NONE
        )
        rest_api_props = apigateway.RestApiProps(default_method_options=method_options)
        runtime_code_path = pathlib.Path(__file__).resolve().parent.joinpath("runtime")
        asset_bundling_command = (
            "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
        )
        function_props = lambda_.FunctionProps(
            runtime=cast(lambda_.Runtime, lambda_.Runtime.PYTHON_3_7),
            code=lambda_.Code.from_asset(
                str(runtime_code_path),
                bundling=cdk.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_7.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        asset_bundling_command,
                    ],
                ),
            ),
            handler="app.lambda_handler",
        )
        apigateway_lambda.ApiGatewayToLambda(
            self,
            "ApiGatewayToLambda",
            api_gateway_props=rest_api_props,
            lambda_function_props=function_props,
        )
