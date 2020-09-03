import sys
import subprocess

'''
A whois service using 'sys' and 'subprocess'.
--------------------------------------------

execution::
-----------
takes two arguments [host, port]
structure:: python whois-service.py <host> <port>
example::   python whois-service.py http://whois.arin.net/ 43

conditions::
------------
if no <host> if provided
- the script will use a fallback host (whois.dk-hostmaster.dk)

if no <port> is provided
- the script will use a fallback port (43)

exceptions::
------------
on empty response
- Couldn't find host <host>

on response code 68
- Couldn't get connection to <host>

on default error
- Unknown error while connecting to <host>
'''


def whois():

    # tries to get second argument
    try:
        host = sys.argv[1]
    except:
        host = "whois.dk-hostmaster.dk"
        print(f'Host value missing, using fallback host: {host}')

    # tries to get third argument
    try:
        port = sys.argv[2]
    except:
        port = 43
        print(f'Port value missing, using fallback port: {port}')

    # subprocess calling 'whois' with host and port
    response = subprocess.run(['whois', host, '-p', str(port)], stdout=subprocess.PIPE)

    # decoding bytestring to utf-8 format
    decoded = response.stdout.decode('utf-8')
    response_code = response.returncode

    # connection successfull
    if (response.returncode is 0):
        # response empty
        if ('% This query returned 0 objects.' in decoded):
            raise Exception(f'Couldn\'t find host {host}')

        # valid response
        else:
            return decoded

    # connection error
    elif (response_code is 68):
        raise Exception(f'Couldn\'t get connection to {host}')

    # default error
    else:
        raise Exception(f'Unknown error while connecting to {host}')


# main method
if __name__ == "__main__":
    try:
        response = whois()
        print(response)
    except Exception as error:
        print('Error::', error)
