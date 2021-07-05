import os

from aws_cdk import core as cdk

from deployment import Application

APPLICATION_NAME = "AwsCdkProjectBasic"

app = cdk.App()

dev_env = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)
prod_env = cdk.Environment(account="123456789012", region="eu-west-1")

Application(app, f"{APPLICATION_NAME}-Application-Dev", env=dev_env)
Application(app, f"{APPLICATION_NAME}-Application-Prod", env=prod_env)

app.synth()
