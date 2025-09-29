# from urllib import request
from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        name=request.form.get("name")
        age=request.form.get("age")
        print(f"Received Name: {name}, Age: {age}")
        return jsonify({"name":name,"age":age}), 200
    return render_template("form.html")

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    app.run(debug=True)