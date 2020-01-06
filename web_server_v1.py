import socket


def parsehttp(http):
    request, *headers, _, body = http.split('\r\n')
    method, path, protocol = request.split(' ')
    headers = dict(line.split(':', maxsplit=1) for line in headers)
    return method, path, protocol, headers, body


def http_response(response):
    formatted_response = "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/html\r\n\r\n{}\r\n".format(
        len(response), response)
    return formatted_response


with socket.socket() as s:
    s.bind(('localhost', 8000))
    while True:
        s.listen(1)
        conn, addr = s.accept()

        with conn:
            request = conn.recv(1024).decode('utf-8')
            print(request)

            print("Response - \n")
            print(http_response('Hello World'))

            conn.sendall(http_response('Hello World').encode('utf-8'))
