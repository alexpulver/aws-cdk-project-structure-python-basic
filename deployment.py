from typing import Any

from aws_cdk import core as cdk

from api.infrastructure import Api


class UUID4GeneratorBackend(cdk.Stack):
    # pylint: disable=redefined-builtin
    # The 'id' parameter name is CDK convention.
    def __init__(self, scope: cdk.Construct, id: str, **kwargs: Any) -> None:
        super().__init__(scope, id, **kwargs)

        Api(self, "Api")
