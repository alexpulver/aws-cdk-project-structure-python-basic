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
# [Optional] Needed to upgrade dependencies and cleanup unused packages
pip install pip-tools==6.1.0
./scripts/install-deps.sh
./scripts/run-tests.sh
```

### [Optional] Upgrade AWS CDK Toolkit version
```bash
vi package.json  # Update "aws-cdk" package version
./scripts/install-deps.sh
./scripts/run-tests.sh
```

### [Optional] Upgrade dependencies (ordered by constraints)
Consider [AWS CDK Toolkit (CLI)](https://docs.aws.amazon.com/cdk/latest/guide/reference.html#versioning) compatibility 
when upgrading AWS CDK packages version.

```bash
pip-compile --upgrade api/runtime/requirements.in
pip-compile --upgrade requirements.in
pip-compile --upgrade requirements-dev.in
./scripts/install-deps.sh
# [Optional] Cleanup unused packages
pip-sync api/runtime/requirements.txt requirements.txt requirements-dev.txt
./scripts/run-tests.sh
```

## Deploy the application to development environment
The `UUIDGeneratorBackend-Dev` stack uses your default account and region.
```bash
npx cdk deploy UUIDGeneratorBackend-Dev
```

Example output for `npx cdk deploy UUIDGeneratorBackend-Dev` stack:
```text
 ✅  UUIDGeneratorBackend-Dev

Outputs:
UUIDGeneratorBackend-Dev.APIApiGatewayToLambdaLambdaRestApiEndpointCDACAFAE = https://qtjok31m4c.execute-api.eu-west-1.amazonaws.com/prod/
```

## Delete the stack
```bash
npx cdk destroy UUIDGeneratorBackend-Dev
```

## Testing the web API

Example output for `curl https://qtjok31m4c.execute-api.eu-west-1.amazonaws.com/prod/`: 
```bash
Hello, CDK! Here is your UUID4: {'uuid': '8b7e99ac-c44b-46ac-990d-22e253b08be4'}
```
