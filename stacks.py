from aws_cdk import core as cdk

from api.infrastructure import Api


class Application(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        Api(self, 'Api')
