#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler

class myRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):  
    try:  
        print('path: --->{}<---'.format(self.path))
        print('header:------------')
        for k,v in self.headers.items():
          print('name: {} wert: {}'.format(k,v))
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
  
        #send data to client  
        self.wfile.write(b'Eine Antwort auf GET')
        return  

    except:  
      self.send_error(404, 'file not found')
      raise

  def print_headers(self):
    print('header:------')
    for k,v in self.headers.items():
      print('name: {} wert: {}'.format(k,v))

  def do_POST(self):
    try:  
        print('path: --->{}<---'.format(self.path))
        self.print_headers()
        datlen = int(self.headers['Content-Length'])
        #print('----Länge-------',datlen)
        data=self.rfile.read(datlen)
        print('Bekam:\n{}'.format(data))
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
  
        #send data to client  
        data = b'... und der Server sagt:\n' + data
        self.wfile.write(data)
        return  

    except:  
      self.send_error(404, 'file not found')
      raise

  def do_PUT(self):
    self.do_GET()

def run():  
  print('http server is starting...')
  serv = HTTPServer(('',8080),myRequestHandler)
  print('http server is running...')
  serv.serve_forever()

if __name__ == '__main__':
  run()
