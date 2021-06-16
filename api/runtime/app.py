import json
from typing import Any, Dict

import requests


def handler(event: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
    print(f"request: {json.dumps(event)}")
    result = requests.get("https://httpbin.org/uuid")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": f"Hello, CDK! Here is your UUID4: {result.json()}\n",
    }
