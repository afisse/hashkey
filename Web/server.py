import sys
import socket


class Body:
    def __init__(self, children):
        self.children = children
    def toString(self):
        inside = ""
        for child in self.children:
            inside += child.toString()
        return "<body>" + inside + "</body>"

class Title:
    def __init__(self, content):
        self.content = content
    def toString(self):
        return "<title>" + self.content.toString() + "</title>"

class Paragraph:
    def __init__(self, content):
        self.content = content
    def toString(self):
        return "<p>" + self.content.toString() + "</p>"

class Text:
    def __init__(self, content):
        self.content = content
    def toString(self):
        return self.content

def answer(client, content):
    if method == "GET":
        msg = "HTTP/1.0 200 OK\nContent-Type:text/html\nContent-Length:"+str(len(content))+"\n\n" + content
        print msg
        client.send(msg)

host = ""
port = int(sys.argv[1])
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
client, addr = server.accept()
print 'Connected by', addr
while 1:
    data = client.recv(1024)
    if not data: break
    response = data.split("\n")

    method = response[0].split()[0]
    path = response[0].split()[1]
    protocol = response[0].split()[2]

    headers = {}
    for x in response[1:-2]:
        key = x.split(":", 1)[0].strip()
        value = x.split(":", 1)[1].strip()
        headers[key] = value
    page = Body([Paragraph(Text("this is an example"))])
    content = page.toString()
    answer(client, content)

client.close()

