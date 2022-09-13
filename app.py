import os

import aws_cdk as cdk

import constants
from component import UuidGeneratorBackend

app = cdk.App()

UuidGeneratorBackend(
    app,
    constants.APP_NAME + "Sandbox",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

UuidGeneratorBackend(
    app,
    constants.APP_NAME + "Production",
    env=cdk.Environment(account="111111111111", region="eu-west-1"),
)

app.synth()
