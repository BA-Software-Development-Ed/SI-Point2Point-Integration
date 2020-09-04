import requests
import sys


def client():

    host = None
    port = None
    payload = None

    try:
        host = sys.argv[1]
        port = sys.argv[2]
        payload = sys.argv[3]
    except:
        if host is None:
            host = 'http://127.0.0.1'
            print(f'Notice:: Host value missing, using fallback host: {host}')

        if port is None:
            port = 6666
            print(f'Notice:: Port value missing, using fallback port: {port}')

        if payload is None:
            payload = 'default payload'
            print(f'Notice:: Payload value missing, using fallback payload: "{payload}"')

    try:
        response = requests.post(f'{host}:{port}/', data=payload)
    except:
        raise Exception(f'Couldn\'t get connection to {host}')

    return response.text


# main method
if __name__ == "__main__":
    try:
        response = client()
        print(response)
    except Exception as error:
        print('Error::', error)
