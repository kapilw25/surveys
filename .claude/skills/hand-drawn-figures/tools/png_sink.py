#!/usr/bin/env python3
"""Receive a data-URL PNG from the browser and write it to disk.

The Chrome tool can render a page but cannot save a file, and a sandboxed page cannot
write to the filesystem. So the page POSTs its `toPng()` data URL here and this decodes it.

  usage:  python3 png_sink.py /abs/path/out.png [port]
  page:   await fetch('http://127.0.0.1:8932/', {method:'POST', body: dataUrl})
"""
import base64, http.server, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "out.png"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8932


class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n).decode()
        b64 = re.sub(r"^data:image/\w+;base64,", "", body)
        with open(OUT, "wb") as f:
            f.write(base64.b64decode(b64))
        print(f"wrote {OUT} ({len(b64)} b64 chars)", flush=True)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"ok")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print(f"png_sink listening on 127.0.0.1:{PORT} -> {OUT}", flush=True)
    http.server.HTTPServer(("127.0.0.1", PORT), H).serve_forever()
