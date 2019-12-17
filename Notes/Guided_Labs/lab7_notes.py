#!/usr/bin/env python

import argparse

import urllib.request

remote_server_host = 'http://www.cnn.com'

class HTTPClient:
    def __init__(self,host):
        self.host = host

    def fetch(self):
        response = urllib.request.urlopen(self.host)
        data = response.read()
        text = data.decode('utf-8')
        return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host',action='store',dest='host',default=remote_server_host)

    given_args = parser.parse_args()
    host = given_args.host
    client = HTTPClient(host)
    print(client.fetch())

