import os

from aws_cdk import core as cdk

from stacks import Application


app = cdk.App()

dev_env = cdk.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'], region=os.environ['CDK_DEFAULT_REGION'])
prod_env = cdk.Environment(account='123456789012', region='eu-west-1')

Application(app, 'AwsCdkProjectDev', env=dev_env)
Application(app, 'AwsCdkProjectProd', env=prod_env)

app.synth()
