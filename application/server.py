"""Small standard-library HTTP host for the local workflow prototype."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from . import store, workflow

WEB = Path(__file__).resolve().parent / "static"


class Handler(BaseHTTPRequestHandler):
    def send(self, code, body, content_type="application/json; charset=utf-8"):
        raw = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        path=urlparse(self.path).path
        if path=="/api/state":
            self.send(200,json.dumps(store.state(),ensure_ascii=False))
        elif path in ("/","/index.html"):
            self.send(200,(WEB/"index.html").read_bytes(),"text/html; charset=utf-8")
        elif path=="/app.js":
            self.send(200,(WEB/"app.js").read_bytes(),"text/javascript; charset=utf-8")
        elif path=="/health": self.send(200,'{"ok":true}')
        else: self.send(404,'{"error":"not found"}')

    def do_POST(self):
        if urlparse(self.path).path!="/api/action":
            return self.send(404,'{"error":"not found"}')
        try:
            length=int(self.headers.get("Content-Length","0"))
            if length>65536: raise ValueError("درخواست بیش از حد بزرگ است.")
            data=json.loads(self.rfile.read(length) or b"{}")
            result=workflow.act(data)
            self.send(200,json.dumps({"ok":True,"state":result},ensure_ascii=False))
        except (ValueError,KeyError,TypeError,json.JSONDecodeError) as exc:
            self.send(400,json.dumps({"ok":False,"error":str(exc)},ensure_ascii=False))

    def log_message(self, fmt, *args):
        print("[%s] %s"%(self.log_date_time_string(),fmt%args))


def main():
    store.init()
    host="127.0.0.1"; port=8765
    print(f"Cutover local workflow is running at http://{host}:{port}")
    print(f"Local database: {store.DB_PATH}")
    ThreadingHTTPServer((host,port),Handler).serve_forever()
