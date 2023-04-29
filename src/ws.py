"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Wolf Paulus (https://wolfpaulus.com)
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import is_prime
from json import load, dumps

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/health":
            status, content = 200, "OK"
        elif self.path == "/" or self.path.startswith("/?number="):
            status = 200
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            result = f"{number} is {'prime' if is_prime(int(number)) else 'composite'}." if number.isnumeric() else ""
            if self.headers.get("Content-Type") == "application/json":  # Checks if it's a json request.
                if number.isnumeric():  # If it's a number
                    data = {"number": number, "prime": is_prime(number), "label": "erau399"}
                    status, content = 200, dumps(data)
                else:
                    status, content = 400, "Your request sucks."
            else:
                with open('./response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    content = f.read().format(path=self.path, time=asctime(), result=result)
        else:
            status, content = 404, "Not Found"
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
