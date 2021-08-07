import os

from aws_cdk import core as cdk

CDK_APP_NAME = "UUIDGeneratorBackend"

DEV_ENV = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)

PROD_ENV = cdk.Environment(account="111111111111", region="eu-west-1")
