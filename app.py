import os

import aws_cdk as cdk

import constants
from component import UuidGeneratorBackendComponent

app = cdk.App()

UuidGeneratorBackendComponent(
    app,
    f"{constants.APP_NAME}Component-Sandbox",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

UuidGeneratorBackendComponent(
    app,
    f"{constants.APP_NAME}Component-Production",
    env=cdk.Environment(account="111111111111", region="eu-west-1"),
)

app.synth()
