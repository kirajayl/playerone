import http.server
import mimetypes

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        mt = getattr(self, 'mimetype', mimetypes.guess_type(self.path)[0] or 'application/octet-stream')
        self.send_header('Content-Type', mt + '; charset=utf-8')
        super().end_headers()

http.server.HTTPServer(('', 8080), UTF8Handler).serve_forever()