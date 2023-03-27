import dns.resolver
import dns.message
import dns.rdatatype
import socketserver

class DNSServer(socketserver.UDPServer):
    def handle_request(self, data):
        request = dns.message.from_wire(data)
        qname = request.question[0].name.to_text()
        qtype = request.question[0].rdtype
        response = dns.message.make_response(request)
        
        if qtype == dns.rdatatype.A:
            answer = dns.rrset.from_text(qname, 300, dns.rdataclass.IN, dns.rdatatype.A, '127.0.0.1')
        elif qtype == dns.rdatatype.AAAA:
            answer = dns.rrset.from_text(qname, 300, dns.rdataclass.IN, dns.rdatatype.AAAA, '::1')
        else:
            return None

        response.answer.append(answer)
        response.flags |= dns.flags.QR | dns.flags.RA 

        return response.to_wire()

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        response = self.server.handle_request(data)

        if response is not None:
            socket.sendto(response, self.client_address)

if __name__ == '__main__':
    server = DNSServer(('localhost', 53), DNSHandler)
    server.serve_forever()