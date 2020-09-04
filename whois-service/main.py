import sys
import subprocess


def whois():

    host = None
    port = None

    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except:
        if host is None:
            host = "whois.dk-hostmaster.dk"
            print(f'Notice:: Host value missing, using fallback host: {host}')

        if port is None:
            port = 43
            print(f'Notice:: Port value missing, using fallback port: {port}')

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
