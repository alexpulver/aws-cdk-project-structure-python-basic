import aws_cdk as cdk

import constants
from deployment import UuidGeneratorBackend

app = cdk.App()

# Development
UuidGeneratorBackend(app, f"{constants.CDK_APP_NAME}-Dev", env=constants.DEV_ENV)

# Production
UuidGeneratorBackend(app, f"{constants.CDK_APP_NAME}-Prod", env=constants.PROD_ENV)

app.synth()
