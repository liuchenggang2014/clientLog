from google.auth import jwt
import requests
import json
import base64

from requests.models import Response
from werkzeug.datastructures import IfRange

# Message data
json_payload = [
    {
        "id": "202006141124",
        "price": "$1.99",
        "product": "shirt"

    },
    {
        "id": "3",
        "price": "$3.99",
        "product": "shirt"

    },
    {
        "id": "4",
        "price": "$4.99",
        "product": "shirt"

    },
    {
        "id": "4",
        "price": "$4.99",
        "product": "shirt"

    },
    {
        "id": "6",
        "price": "$6.99",
        "product": "shirt"

    },
    {
        "id": "7",
        "price": "$7.99",
        "product": "shirt"

    },
    {
        "id": "7",
        "price": "$7.99",
        "product": "shirt"

    },
    {
        "id": "9",
        "price": "$9.99",
        "product": "shirt"

    },
    {
        "id": "9",
        "price": "$9.99",
        "product": "shirt"

    },
]

# change the jwt_url as the new deploy'e cloud run's endpoint
jwt_url = 'https://get-pubsub-token-gygrgrxnnq-uc.a.run.app/api'
topic_url = "https://pubsub.googleapis.com/v1/projects/cliu201/topics/cliu201-topic1:publish"


def getToken():
    try:
        r = requests.get(jwt_url, timeout=30)
        # print(r.url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# Publish the message
def publish_with_jwt_request(access_token, encoded_element, url):
    # Request Headers
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'content-type': 'application/json'
    }
    # Request json data
    json_data = {
        "messages": [
            {
                "data": encoded_element,
                "attributes": {"somekey": "somevalue"}
            }
        ]
    }

    # Get response data
    response = requests.post(url, headers=headers, json=json_data)
    if response.status_code == 401:
        return 401

    print(response.status_code, response.content)


def main():
    response = getToken()
    access_token = json.loads(response)['access_token']
    # print(jwt_token)
    # print(a)
    for element in json_payload:
        dumped_element = json.dumps(element)
        message_bytes = dumped_element.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        encoded_element = base64_bytes.decode('ascii')
        print(encoded_element)
        publish_with_jwt_request(access_token, encoded_element, topic_url)

        
if __name__ == '__main__':
    main()


