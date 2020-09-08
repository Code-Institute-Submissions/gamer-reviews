{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\napp = Flask(__name__)\n\napp.config[\"MONGO_DBNAME\"] = 'gamer-reviews'\napp.config[\"MONGO_URI\"] = 'mongodb+srv://joe:Drumgoon6894@gamerreview.85ibj.mongodb.net/gamer-reviews?retryWrites=true&w=majority'\n\nmongo = PyMongo(app)\n\n@app.route('/')\n@app.route('/get_reviews')\ndef get_reviews():\n    return render_template(\"reviews.html\", reviews=mongo.db.reviews.find())\n    \nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True)\n","undoManager":{"mark":106,"position":100,"stack":[[{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"],"id":92},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":93},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["b"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["s"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"remove","lines":["i"],"id":94}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"],"id":95},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["n"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["."]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["b"],"id":96},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["j"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["e"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["c"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["t"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["i"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":[" "],"id":97},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["i"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["m"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["p"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["o"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["t"],"id":98}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":[" "],"id":99},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["O"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["b"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["j"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["e"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["c"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["I"],"id":100},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":21},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":101},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["a"]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["p"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["p"]}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["."],"id":102},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["c"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["o"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["m"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["m"],"id":103}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["n"],"id":104}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["f"],"id":105},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["i"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":12},"action":"insert","lines":["[]"],"id":106}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":13},"action":"insert","lines":["\"\""],"id":107}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["M"],"id":108},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["O"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["N"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["G"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["O"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["_"],"id":109},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["D"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["B"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["N"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["A"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["M"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["E"]}],[{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":[" "],"id":110},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":[" "],"id":111}],[{"start":{"row":7,"column":29},"end":{"row":7,"column":31},"action":"insert","lines":["''"],"id":112}],[{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["g"],"id":113},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["a"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["m"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["e"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["-"],"id":114},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["r"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["e"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["v"]},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["i"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["e"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["w"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":44},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":115},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["a"]}],[{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["p"],"id":116},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["p"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["."]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["c"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["o"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["f"],"id":117},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["i"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["g"]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":12},"action":"insert","lines":["[]"],"id":118}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"insert","lines":["\"\""],"id":119}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["M"],"id":120},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["O"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["N"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["G"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["O"]}],[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["_"],"id":121},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["U"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["R"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["I"]}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":[" "],"id":122},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["-"]}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["-"],"id":123}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["="],"id":124}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":[" "],"id":125}],[{"start":{"row":8,"column":26},"end":{"row":8,"column":28},"action":"insert","lines":["''"],"id":126}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":122},"action":"insert","lines":["mongodb+srv://joe:<password>@gamerreview.85ibj.mongodb.net/<dbname>?retryWrites=true&w=majority"],"id":127}],[{"start":{"row":8,"column":93},"end":{"row":8,"column":94},"action":"remove","lines":[">"],"id":128},{"start":{"row":8,"column":92},"end":{"row":8,"column":93},"action":"remove","lines":["e"]},{"start":{"row":8,"column":91},"end":{"row":8,"column":92},"action":"remove","lines":["m"]},{"start":{"row":8,"column":90},"end":{"row":8,"column":91},"action":"remove","lines":["a"]},{"start":{"row":8,"column":89},"end":{"row":8,"column":90},"action":"remove","lines":["n"]},{"start":{"row":8,"column":88},"end":{"row":8,"column":89},"action":"remove","lines":["b"]},{"start":{"row":8,"column":87},"end":{"row":8,"column":88},"action":"remove","lines":["d"]},{"start":{"row":8,"column":86},"end":{"row":8,"column":87},"action":"remove","lines":["<"]}],[{"start":{"row":8,"column":86},"end":{"row":8,"column":87},"action":"insert","lines":["g"],"id":129},{"start":{"row":8,"column":87},"end":{"row":8,"column":88},"action":"insert","lines":["a"]},{"start":{"row":8,"column":88},"end":{"row":8,"column":89},"action":"insert","lines":["m"]},{"start":{"row":8,"column":89},"end":{"row":8,"column":90},"action":"insert","lines":["e"]},{"start":{"row":8,"column":90},"end":{"row":8,"column":91},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":91},"end":{"row":8,"column":92},"action":"insert","lines":["-"],"id":130},{"start":{"row":8,"column":92},"end":{"row":8,"column":93},"action":"insert","lines":["r"]},{"start":{"row":8,"column":93},"end":{"row":8,"column":94},"action":"insert","lines":["e"]},{"start":{"row":8,"column":94},"end":{"row":8,"column":95},"action":"insert","lines":["v"]},{"start":{"row":8,"column":95},"end":{"row":8,"column":96},"action":"insert","lines":["i"]},{"start":{"row":8,"column":96},"end":{"row":8,"column":97},"action":"insert","lines":["e"]},{"start":{"row":8,"column":97},"end":{"row":8,"column":98},"action":"insert","lines":["w"]},{"start":{"row":8,"column":98},"end":{"row":8,"column":99},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"remove","lines":[">"],"id":131},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"remove","lines":["d"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":["r"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["o"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["w"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["s"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["s"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["a"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["p"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"remove","lines":["<"]}],[{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["D"],"id":132},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["r"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["u"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["m"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["g"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["o"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["o"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["n"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["6"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["8"]}],[{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["9"],"id":133},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["4"]}],[{"start":{"row":8,"column":130},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":134},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["m"],"id":135},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["o"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["n"]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["g"]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":[" "],"id":136},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":[" "],"id":137},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["P"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["y"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["m"]},{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["o"]},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["g"],"id":138},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["o"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":17},"action":"insert","lines":["()"],"id":139}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["a"],"id":140},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["p"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["p"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["p"]}],[{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"remove","lines":["p"],"id":141}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"remove","lines":["m"],"id":142}],[{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["M"],"id":143}],[{"start":{"row":10,"column":20},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":144},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""],"id":145},{"start":{"row":10,"column":20},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":15},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":146},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["@"]}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"],"id":147},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["p"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["."]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["o"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["y"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["e"],"id":148}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["e"],"id":149},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["y"]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["u"],"id":150},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["()"],"id":151}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":13},"action":"insert","lines":["''"],"id":152}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["/"],"id":153},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["g"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["e"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["t"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["t"],"id":154},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["a"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["s"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["k"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":["s"],"id":155},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["k"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["s"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["a"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["t"]}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["r"],"id":156},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["e"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["v"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["i"]},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["e"]},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["w"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["o"],"id":157},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["l"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["l"]},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":["e"]},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["h"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["g"],"id":158},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["t"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["_"]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["r"],"id":159},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["e"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["v"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["i"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["e"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["w"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":[","],"id":160}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":[" "],"id":161},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["r"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["e"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["n"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["d"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["e"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["_"],"id":162},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["t"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["m"],"id":163},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["p"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["l"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["a"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"],"id":164}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":[","],"id":165}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[" "],"id":166},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["r"]},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["e"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["i"],"id":167},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["r"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["e"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["c"]},{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":[","],"id":168}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":[" "],"id":169},{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":["r"]},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"insert","lines":["q"],"id":170},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["u"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["e"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"insert","lines":["s"]},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"insert","lines":["t"]},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"insert","lines":[","]}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"insert","lines":[" "],"id":171},{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"insert","lines":["u"]},{"start":{"row":1,"column":62},"end":{"row":1,"column":63},"action":"insert","lines":["r"]},{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"insert","lines":["l"]}],[{"start":{"row":1,"column":64},"end":{"row":1,"column":65},"action":"insert","lines":["_"],"id":172},{"start":{"row":1,"column":65},"end":{"row":1,"column":66},"action":"insert","lines":["f"]},{"start":{"row":1,"column":66},"end":{"row":1,"column":67},"action":"insert","lines":["o"]},{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"remove","lines":["'"],"id":173},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["n"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["i"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["a"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["g"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["a"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":[" "]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["."]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["."]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["."]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":[" "]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["d"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["l"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["r"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["o"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["w"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":[" "]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["o"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["l"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["l"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["e"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["H"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":["'"],"id":174}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["r"],"id":175},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":13},"action":"remove","lines":["re"],"id":176},{"start":{"row":15,"column":11},"end":{"row":15,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":28},"action":"insert","lines":["()"],"id":177}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":29},"action":"insert","lines":["\"\""],"id":178}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["r"],"id":179},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["e"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["v"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["i"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["e"]},{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["w"]},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["s"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["."]}],[{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["h"],"id":180},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["t"]},{"start":{"row":15,"column":38},"end":{"row":15,"column":39},"action":"insert","lines":["m"]},{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":[","],"id":181}],[{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":[" "],"id":182}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["t"],"id":183},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["a"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["s"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["k"]}],[{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"remove","lines":["k"],"id":184},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"remove","lines":["s"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"remove","lines":["a"]},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"remove","lines":["t"]}],[{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["r"],"id":185},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["e"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["v"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["i"]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["e"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["w"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["="],"id":186},{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["m"]},{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["o"]},{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["g"],"id":187},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["o"]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["."]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["d"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["b"]},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["."]}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["r"],"id":188},{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["e"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["v"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["i"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":["e"]},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":["w"]},{"start":{"row":15,"column":66},"end":{"row":15,"column":67},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":67},"end":{"row":15,"column":68},"action":"insert","lines":["."],"id":189},{"start":{"row":15,"column":68},"end":{"row":15,"column":69},"action":"insert","lines":["f"]},{"start":{"row":15,"column":69},"end":{"row":15,"column":70},"action":"insert","lines":["i"]},{"start":{"row":15,"column":70},"end":{"row":15,"column":71},"action":"insert","lines":["n"]},{"start":{"row":15,"column":71},"end":{"row":15,"column":72},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":72},"end":{"row":15,"column":74},"action":"insert","lines":["()"],"id":190}],[{"start":{"row":17,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["if __name__ == '__main__':","    app.run(host=os.environ.get('IP'), ","    port=int(os.environ.get('PORT')),","    debug=True)","    "],"id":193}],[{"start":{"row":17,"column":0},"end":{"row":20,"column":23},"action":"insert","lines":["if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":194}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":[")"],"id":200}],[{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"remove","lines":[","],"id":200}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":45},"action":"remove","lines":["port=int(os.environ.get('PORT')))"],"id":201},{"start":{"row":19,"column":8},"end":{"row":19,"column":12},"action":"remove","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "]},{"start":{"row":18,"column":38},"end":{"row":19,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"insert","lines":[")"],"id":202}],[{"start":{"row":19,"column":45},"end":{"row":20,"column":0},"action":"remove","lines":["",""],"id":203},{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"remove","lines":[","]}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":23},"action":"remove","lines":[")"],"id":204},{"start":{"row":20,"column":21},"end":{"row":20,"column":22},"action":"remove","lines":["e"]},{"start":{"row":20,"column":20},"end":{"row":20,"column":21},"action":"remove","lines":["u"]},{"start":{"row":20,"column":19},"end":{"row":20,"column":20},"action":"remove","lines":["r"]},{"start":{"row":20,"column":18},"end":{"row":20,"column":19},"action":"remove","lines":["T"]},{"start":{"row":20,"column":17},"end":{"row":20,"column":18},"action":"remove","lines":["="]},{"start":{"row":20,"column":16},"end":{"row":20,"column":17},"action":"remove","lines":["g"]},{"start":{"row":20,"column":15},"end":{"row":20,"column":16},"action":"remove","lines":["u"]},{"start":{"row":20,"column":14},"end":{"row":20,"column":15},"action":"remove","lines":["b"]},{"start":{"row":20,"column":13},"end":{"row":20,"column":14},"action":"remove","lines":["e"]},{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":["d"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":12},"action":"remove","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":0},"end":{"row":21,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":279,"mode":"ace/mode/python"}},"timestamp":1599560223844}