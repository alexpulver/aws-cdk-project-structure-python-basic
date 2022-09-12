from typing import Any

import aws_cdk as cdk
from constructs import Construct

from api.infrastructure import API


class UuidGeneratorBackend(cdk.Stack):
    def __init__(self, scope: Construct, id_: str, **kwargs: Any) -> None:
        super().__init__(scope, id_, **kwargs)

        api = API(self, "API")
        cdk.CfnOutput(
            self,
            "APIEndpoint",
            # API doesn't disable create_default_stage, hence URL will be defined
            value=api.api_gateway_http_api.url,  # type: ignore
        )
