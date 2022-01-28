from flask import Flask, request, jsonify
from mcquery import mcquery

app = Flask(__name__)


@app.route('/<string:ip>/')
def server(ip):
    try:
        with mcquery(host=ip, port=19132, timeout=30) as data:
            player = jsonify(Players=data.players)
            return player
      except:
        return "<br><br><br><br><br><br><br><center><h2>Timed Out</h2></center>", 400



app.run(host='0.0.0.0', port=8080, debug=True)
