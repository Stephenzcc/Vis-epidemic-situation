from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from pyhanlp import *
import string
import utils

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm": str(data[0]), "suspect": str(data[1]), "heal": str(data[2]), "dead": str(data[3])})

@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[7:]: #前7条数据是null
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})

@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]: #前7条数据是null
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})

@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data()
    d = []
    for i in data:
        k = i[0].rstrip('0123456789')
        v = i[0][len(k):]
        ks = HanLP.extractKeyword(k, 2)
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"kws": d})

@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/ajax', methods=["get", "post"])
def ajax():
    name = request.values.get("name")
    score = request.values.get("score")
    print(f"name:{name}, score:{score}")
    return '10000'



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)

