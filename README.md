# Recommended AWS CDK project structure for Python basic applications

#### Create development environment
See [Getting Started With the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
for additional details and prerequisites

```bash
# Clone the code
git clone https://github.com/alexpulver/aws-cdk-project-structure-python-basic
cd aws-cdk-project-structure-python-basic

# Create Python virtual environment and install the dependencies
python3 -m venv .venv
source .venv/bin/activate
./install-deps.sh

## Upgrading dependencies
pip-compile --upgrade requirements.in
./install-deps.sh
```

#### Deploy the stack
```bash
npx cdk deploy AwsCdkProjectDev
```

#### Delete the stack
```bash
npx cdk destroy AwsCdkProjectDev
```
