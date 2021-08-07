from aws_cdk import core as cdk

import constants
from deployment import UUIDGeneratorBackend

app = cdk.App()

# Development
UUIDGeneratorBackend(app, f"{constants.CDK_APP_NAME}-Dev", env=constants.DEV_ENV)

# Production
UUIDGeneratorBackend(app, f"{constants.CDK_APP_NAME}-Prod", env=constants.PROD_ENV)

app.synth()
