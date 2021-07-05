# Recommended AWS CDK project structure for basic Python applications

## Create development environment
See [Getting Started With the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
for additional details and prerequisites

### Clone the code
```bash
git clone https://github.com/alexpulver/aws-cdk-project-structure-python-basic
cd aws-cdk-project-structure-python-basic
```

### Create Python virtual environment and install the dependencies
```bash
python3.7 -m venv .venv
source .venv/bin/activate
pip install pip-tools==6.1.0  # [Optional] Needed to upgrade dependencies and cleanup unused packages
./scripts/install-deps.sh
./scripts/run-tests.sh
```

### [Optional] Upgrade AWS CDK Toolkit version
```bash
vi package.json  # Update "aws-cdk" package version
./scripts/install-deps.sh
```

### [Optional] Upgrade dependencies (ordered by constraints)
```bash
pip-compile --upgrade api/runtime/requirements.in
pip-compile --upgrade requirements.in
pip-compile --upgrade requirements-dev.in
./scripts/install-deps.sh
pip-sync api/runtime/requirements.txt requirements.txt requirements-dev.txt  # [Optional] Cleanup unused packages
./scripts/run-tests.sh
```

## Deploy the application to development environment
The `AwsCdkProjectDev` stack uses your default account and region.
```bash
npx cdk deploy AwsCdkProjectDev
```

Example output for `npx cdk deploy AwsCdkProjectDev` stack:
```text
AwsCdkProjectDev.ApiApiGatewayToLambdaLambdaRestApiEndpointDA51B1D3 = https://mebs1wbl2f.execute-api.eu-west-1.amazonaws.com/prod/
```

## Delete the stack
```bash
npx cdk destroy AwsCdkProjectDev
```

## Testing the web API
```bash
$ curl https://mebs1wbl2f.execute-api.eu-west-1.amazonaws.com/prod/
Hello, CDK! Here is your UUID4: {'uuid': '8b7e99ac-c44b-46ac-990d-22e253b08be4'}
```