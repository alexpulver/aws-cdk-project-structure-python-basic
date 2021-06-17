# Recommended AWS CDK project structure for Python basic applications

#### Create development environment
See [Getting Started With the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
for additional details and prerequisites

```bash
# Clone the code
git clone https://github.com/alexpulver/aws-cdk-project-structure-python-basic
cd aws-cdk-project-structure-python-basic

# Create Python virtual environment and install the dependencies
python3.7 -m venv .venv
source .venv/bin/activate
./scripts/install-deps.sh
./scripts/run-tests.sh

## Upgrading dependencies (ordered by constraints)
pip install pip-tools==6.1.0
pip-compile --upgrade api/runtime/requirements.in
pip-compile --upgrade requirements.in
pip-compile --upgrade requirements-dev.in
./scripts/install-deps.sh
./scripts/run-tests.sh
```

#### Deploy the stack
```bash
npx cdk deploy AwsCdkProjectDev
```

Example output for `npx cdk deploy AwsCdkProjectDev` stack:

```text
AwsCdkProjectDev.ApiApiGatewayToLambdaLambdaRestApiEndpointDA51B1D3 = https://mebs1wbl2f.execute-api.eu-west-1.amazonaws.com/prod/
```

#### Delete the stack
```bash
npx cdk destroy AwsCdkProjectDev
```

#### Testing the web API
```bash
$ curl https://mebs1wbl2f.execute-api.eu-west-1.amazonaws.com/prod/
Hello, CDK! Here is your UUID4: {'uuid': '8b7e99ac-c44b-46ac-990d-22e253b08be4'}
```