#!/usr/bin/env python

from http.server import HTTPServer, CGIHTTPRequestHandler

serv = HTTPServer(('',8080),CGIHTTPRequestHandler)
serv.serve_forever()

input()
