from flask import Flask, render_template
import simplejson as json


app = Flask(__name__)


@app.route('/route1/')
@app.route('/route1/<name>')
def route1(name=None):
    return name

@app.route('/route2/')
def route2():
    parksList = []
    with open('parks.json', 'r') as f:
        parksList = json.load(f)
    return render_template("template.html", parks=parksList)

if __name__ == "__main__":
    app.run()


