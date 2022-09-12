import os

import aws_cdk as cdk

import constants
from component import UuidGeneratorBackend

SANDBOX_ENV_NAME = "Sandbox"
PRODUCTION_ENV_NAME = "Production"

app = cdk.App()

UuidGeneratorBackend(
    app,
    constants.APP_NAME + SANDBOX_ENV_NAME,
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

UuidGeneratorBackend(
    app,
    constants.APP_NAME + PRODUCTION_ENV_NAME,
    env=cdk.Environment(account="111111111111", region="eu-west-1"),
)

app.synth()
