import os

import aws_cdk as cdk

CDK_APP_NAME = "UuidGeneratorBackend"

DEV_ENV = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)

PROD_ENV = cdk.Environment(account="111111111111", region="eu-west-1")
