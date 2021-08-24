import pathlib
from typing import cast

from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_lambda as lambda_
from aws_cdk import core as cdk
from aws_solutions_constructs import aws_apigateway_lambda as apigateway_lambda


class API(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id_: str) -> None:
        super().__init__(scope, id_)

        rest_api_props = self._create_rest_api_props()
        function_props = self._create_function_props()
        apigateway_lambda.ApiGatewayToLambda(
            self,
            "ApiGatewayToLambda",
            api_gateway_props=rest_api_props,
            lambda_function_props=function_props,
        )

    @staticmethod
    def _create_rest_api_props() -> apigateway.RestApiProps:
        method_options = apigateway.MethodOptions(
            authorization_type=apigateway.AuthorizationType.NONE
        )
        rest_api_props = apigateway.RestApiProps(default_method_options=method_options)
        return rest_api_props

    @staticmethod
    def _create_function_props() -> lambda_.FunctionProps:
        runtime_code_path = pathlib.Path(__file__).parent.joinpath("runtime").resolve()
        asset_bundling_command = (
            "pip install -r requirements.txt -t /asset-output && cp -au . /asset-output"
        )
        lambda_runtime = cast(lambda_.Runtime, lambda_.Runtime.PYTHON_3_7)
        bundling_options = cdk.BundlingOptions(
            # pylint: disable=no-member
            image=lambda_runtime.bundling_image,
            command=[
                "bash",
                "-c",
                asset_bundling_command,
            ],
        )
        function_props = lambda_.FunctionProps(
            runtime=lambda_runtime,
            code=lambda_.Code.from_asset(
                str(runtime_code_path),
                bundling=bundling_options,
            ),
            handler="app.lambda_handler",
        )
        return function_props
