from flask import Flask, request, jsonify,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("calculate",methods=["POST"])
def calculate():
    data:request.json
    num1=float(data["num1"])
    num2=float(data["num2"])
    operator=data["operator"]

    try :
        if operator=="+":
            result=num1+num2
        elif operator=="-":
            result=num1-num2
        elif operator=="*":
            result=num1*num2
        elif operator=="/":

            if num2==0:
                return jsonify({"error":"Division by zero"}),400
            result=num1/num2
        else:
            return jsonify({"result": "Invalid operator"})

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"result": str(e)})
if __name__=="__main__":
    app.run(debug=True)