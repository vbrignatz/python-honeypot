from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

SECRET_KEY = '1234'
# je1ne1suis1pas1un1hackerz

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_GET(self, body=True):
        if self.verify_secretkey():
            # get realapp response
            resp = requests.get('http://realapp:8080/time')

        else:
            # get fakeapp response
            resp = requests.get('http://fakeapp:8080/time')

        # Respond with the requested data
        self.send_response(resp.status_code)
        for k, v in resp.headers.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(resp.content)

    def verify_secretkey(self):
        if 'secretkey' in self.headers.keys():
            if self.headers['secretkey'] == SECRET_KEY:
                return True
        return False

if __name__ == '__main__':
    server_address = ('0', 8080)
    httpd = HTTPServer(server_address, ProxyHTTPRequestHandler)
    print('INFO: Proxy is running')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()