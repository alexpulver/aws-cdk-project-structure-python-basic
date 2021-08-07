import os

from aws_cdk import core as cdk

import constants
from deployment import UUIDGeneratorBackend

app = cdk.App()

# Development
UUIDGeneratorBackend(
    app,
    f"{constants.CDK_APP_NAME}-Dev",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)
# Production
UUIDGeneratorBackend(
    app,
    f"{constants.CDK_APP_NAME}-Prod",
    env=cdk.Environment(account=constants.PROD_ACCOUNT, region=constants.PROD_REGION),
)

app.synth()
