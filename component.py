from typing import Any

import aws_cdk as cdk
from constructs import Construct

from api.infrastructure import Api


class UuidGeneratorBackendComponent(cdk.Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs: Any) -> None:
        super().__init__(scope, id_, **kwargs)

        api = Api(self, "Api")
        cdk.CfnOutput(
            self,
            "ApiEndpoint",
            # Api doesn't disable create_default_stage, hence URL will be defined
            value=api.api_gateway_http_api.url,  # type: ignore
        )
