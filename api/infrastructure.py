from pathlib import Path

from aws_cdk import aws_apigateway as apigateway
from aws_cdk import aws_lambda as lambda_
from aws_cdk import core as cdk
from aws_solutions_constructs import aws_apigateway_lambda as apigateway_lambda


class Api(cdk.Construct):
    _RUNTIME_DIR = Path(__file__).resolve().parent.joinpath("runtime")

    # pylint: disable=redefined-builtin
    # The 'id' parameter name is CDK convention.
    def __init__(self, scope: cdk.Construct, id: str) -> None:
        super().__init__(scope, id)

        method_options = apigateway.MethodOptions(
            authorization_type=apigateway.AuthorizationType.NONE
        )
        rest_api_props = apigateway.RestApiProps(default_method_options=method_options)
        function_props = lambda_.FunctionProps(
            runtime=lambda_.Runtime.PYTHON_3_7,  # type: ignore
            code=lambda_.Code.from_asset(
                str(Api._RUNTIME_DIR),
                bundling=cdk.BundlingOptions(
                    image=lambda_.Runtime.PYTHON_3_7.bundling_image,  # pylint: disable=no-member
                    command=[
                        "bash",
                        "-c",
                        "pip install -r requirements.txt -t /asset-output "
                        "&& cp -au . /asset-output",
                    ],
                ),
            ),
            handler="app.handler",
        )
        apigateway_lambda.ApiGatewayToLambda(
            self,
            "ApiGatewayToLambda",
            api_gateway_props=rest_api_props,
            lambda_function_props=function_props,
        )
