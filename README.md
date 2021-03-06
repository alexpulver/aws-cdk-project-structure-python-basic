# Recommended AWS CDK project structure for basic Python applications
The project implements a UUID generator backend component that uses Amazon API Gateway
and AWS Lambda to generate a UUID with https://httpbin.org/uuid.

![diagram](https://user-images.githubusercontent.com/4362270/147329761-d2834879-de3a-40d0-8af6-6b787dbc895a.png)
\* Diagram generated using https://github.com/pistazie/cdk-dia

## Create a new repository from aws-cdk-project-structure-python-basic
This project is a template. Click “Use this template” (see the screenshot below) in 
the repository [main page](https://github.com/alexpulver/aws-cdk-project-structure-python-basic)
to create your own repository based on alexpulver/aws-cdk-project-structure-python-basic. 

![template](https://user-images.githubusercontent.com/4362270/128629234-31cd275e-6a3f-4a6a-9010-028a0a279950.png)

The instructions below use the aws-cdk-project-structure-python-basic repository.

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
pip install pip-tools==6.4.0
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

## Deploy the component to development environment
The `UuidGeneratorBackend-Dev` stack uses your default AWS account and region.
```bash
npx cdk deploy UuidGeneratorBackend-Dev
```

Example output for `npx cdk deploy UuidGeneratorBackend-Dev` stack:
```text
 ✅  UuidGeneratorBackend-Dev

Outputs:
UuidGeneratorBackend-Dev.ApiEndpoint = https://lsw18met42.execute-api.eu-west-1.amazonaws.com/
```

## Delete the stack
```bash
npx cdk destroy UuidGeneratorBackend-Dev
```

## Testing the API

Below is an example for using the API:

```bash
$ api_endpoint=$(aws cloudformation describe-stacks \
  --stack-name UuidGeneratorBackend-Dev \
  --query 'Stacks[*].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text)

$ curl "${api_endpoint}"
Hello, CDK! Here is your UUID: 8b7e99ac-c44b-46ac-990d-22e253b08be4
```
