from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/sum",methods=["POST"])
def calculate_sum():
     data=request.get_json()
     a=data["a"]
     b=data["b"]
     return jsonify({"sum":a+b})
@app.route("/multiply",methods=["POST"])
def calculate_multiply():
     data=request.get_json()
     a=data["a"]
     b=data["b"]
     return jsonify({"multiplication":a*b})
@app.route("/subtact",methods=["POST"])
def calculate_subtact():
     data=request.get_json()
     a=data["a"]
     b=data["b"]
     return jsonify({"subtraction":a-b})
@app.route("/division",methods=["POST"])
def calculate_division():
     data=request.get_json()
     a=data["a"]
     b=data["b"]
     return jsonify({"division":a/b})

if __name__ == "__main__":
    app.run(debug=True)

