import requests
import json
from flask import Flask
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def createJira():
    url = "https://arishakhtar20thapr.atlassian.net//rest/api/3/issue"

    API_TOKEN = ""

    auth = HTTPBasicAuth("arishakhtar20thapr@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "AR"
        },
        "issuetype": {
        "id": "10005"
        },
        "summary": "JIRA Ticket Issued",
    },
    "update": {}
    } )

    request_data = request.json
    if "comment" in request_data and "/jira" in request_data["comment"]["body"]:
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        return "No Jira ticket issued."

if __name__ == '__main__':
    app.run('0.0.0.0')
