#!/usr/bin/env python3
'''
    App module for numbers api
'''

from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from os import getenv
from utils.utils import isArmstrong, isPerfect, digitSum, isPrime
import requests

app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

@app.route("/api/classify-number")
def get_fun_facts():
    """
        returns fun facts about a number
    """
    number = request.args.get("number", type=int)
    if number is None:
        return make_response(jsonify({"number": request.args.get("number"), "error": True}), 400)
    
    properties = []

    if isArmstrong(number):
        properties.append("armstrong")

    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    fun_fact = ""
    url = f"http://numbersapi.com/{number}/math"
    response = requests.get(url)
    if response.ok:
        fun_fact =response.text

    payload = {
        "number": number,
        "is_prime": isPrime(number),
        "is_perfect": isPerfect(number),
        "properties": properties,
        "digit_sum": digitSum(number),
        "fun_fact": fun_fact
    }
    return  make_response(jsonify(payload), 200) 

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
