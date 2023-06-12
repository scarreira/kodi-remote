#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs

import requests
import json

PORT_NUMBER = 8085
PUBLIC_ENTRY = './public/index.html'
url = "http://kodi:remote@127.0.0.1:8080/jsonrpc"

# This class will handles any incoming request
class handleRoutes(BaseHTTPRequestHandler):
  # Handler for the GET requests
  def do_GET(self):
    if (self.path == '/'):
      file = open(PUBLIC_ENTRY)
      self.sendResponse(file.read(), 200, 'text/html')
      file.close()
      return
    if (self.path.startswith('/api/v1/')):
      if (self.path.endswith('volume-up')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Application.SetVolume","params":{"volume": "increment"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('volume-down')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Application.SetVolume","params":{"volume": "decrement"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.split('?',1)[0].endswith('change-channel')):
        query_components = parse_qs(urlparse(self.path).query)
        channel = query_components["ch"]
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "number' + channel[0]  + '"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.split('?',1)[0].endswith('mute')):
        query_components = parse_qs(urlparse(self.path).query)
        mute = query_components["mute"]
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Application.SetMute", "params": {"mute":' + mute[0] + '}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('channel-up')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "up"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('right')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "right"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('left')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "left"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('channel-down')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "down"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('ok')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "select"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('back')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"Input.ExecuteAction","params":{"action": "back"}}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
      if (self.path.endswith('shutdown')):
        jsonCmd = '{"jsonrpc":"2.0","id":1,"method":"System.Shutdown"}'
        x = requests.post(url, jsonCmd)
        return self.sendResponse(x.text, 200, 'application/json')
    else:
      return self.sendResponse('{"message" : "Not found"}', 404, 'application/json')

  def sendResponse(self, res, status, type):
    self.send_response(status)
    self.send_header('Content-type', type)
    # Header to avoid cors problems
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    # Send the html message
    self.wfile.write(res)
    return

try:
  # Create a web server and define the handler to manage the incoming requests
  server = HTTPServer(('', PORT_NUMBER), handleRoutes)
  print 'Started http server on port ' , PORT_NUMBER
  # Wait forever for incoming http requests
  server.serve_forever()

except KeyboardInterrupt:
  print '\nFarewell my friend.'
  server.socket.close()


