import os

from sanic import Sanic, response

app = Sanic(__name__)

@app.route("/foo")
def foo(request):
    return response.text("hello")

if __name__ == "__main__":
    dev = os.getenv('ENV') == 'dev'
    app.run(host="0.0.0.0", debug=dev, port=3001)
