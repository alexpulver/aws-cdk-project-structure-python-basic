import os

from aws_cdk import core as cdk

from deployment import UUID4GeneratorBackend

app = cdk.App()

dev_env = cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"]
)
prod_env = cdk.Environment(account="123456789012", region="eu-west-1")

UUID4GeneratorBackend(app, f"{UUID4GeneratorBackend.__name__}-Dev", env=dev_env)
UUID4GeneratorBackend(app, f"{UUID4GeneratorBackend.__name__}-Prod", env=prod_env)

app.synth()
