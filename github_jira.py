import requests
from requests.auth import HTTPBasicAuth
import json
from flask import request
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://arishakhtar20thapr.atlassian.net/rest/api/3/issue"

    API_TOKEN=""

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
                            "text": "Order entry fails when selecting supplier.",
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
        return "Invalid request body"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
