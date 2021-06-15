import json

import requests


def handler(event, context):
    print(f"request: {json.dumps(event)}")
    result = requests.get("https://httpbin.org/uuid")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": f"Hello, CDK! Here is your UUID4: {result.json()}\n",
    }
