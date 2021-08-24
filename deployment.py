from typing import Any

from aws_cdk import core as cdk

from api.infrastructure import API


class UUIDGeneratorBackend(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id_: str, **kwargs: Any) -> None:
        super().__init__(scope, id_, **kwargs)

        api = API(self, "API")
        cdk.CfnOutput(
            self,
            "APIEndpointURL",
            # API doesn't disable create_default_stage, hence URL will be defined
            value=api.http_api.url,  # type: ignore
        )
