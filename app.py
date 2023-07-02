import os

import aws_cdk as cdk

import constants
from service.service_stack import ServiceStack

app = cdk.App()

# Service sandbox stack
ServiceStack(
    app,
    f"{constants.APP_NAME}-Service-Sandbox",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

# Service production stack
ServiceStack(
    app,
    f"{constants.APP_NAME}-Service-Production",
    env=cdk.Environment(account="111111111111", region="eu-west-1"),
)

app.synth()
