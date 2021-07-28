from typing import Any

from aws_cdk import core as cdk

from api.infrastructure import API


class UUID4GeneratorBackend(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id_: str, **kwargs: Any) -> None:
        super().__init__(scope, id_, **kwargs)

        API(self, "API")
