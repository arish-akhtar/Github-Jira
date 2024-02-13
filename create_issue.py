# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://arishakhtar20thapr.atlassian.net//rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0MRfwJyNnAflJXcV-crvqOs4Tb8vY8NFfd28Latnnn2Sm8SIRnik1Wif_2gP3qLQvmr-gx1sQNyPsNchBXiqUiWmC6RSIqW7LDKJlSlqc852WZAMp8ecrUY_zUGkTI-iDX1VrbV6yTzXj7-S93X5ZOzHjFm2m7oRmq6mc660t5uQ=DD38BB66"

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
    "summary": "JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))