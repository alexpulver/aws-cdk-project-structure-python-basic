import json
from typing import Any, Dict

import requests


def lambda_handler(event: Dict[str, Any], _: Dict[str, Any]) -> Dict[str, Any]:
    print(f"request: {json.dumps(event)}")
    uuid_message = get_uuid_message()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": uuid_message,
    }


def get_uuid_message() -> str:
    response = requests.get("https://httpbin.org/uuid", timeout=30)
    uuid = response.json()["uuid"]
    return f"Hello, CDK! Here is your UUID: {uuid}"
