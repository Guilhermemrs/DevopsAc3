import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')
def primos():

    limite = 100
    
    inicio = 1
    cont = 1
    num = 3
    
    primo = "2, "
    
    while cont < limite:
        Eprimo = 1
        for i in range(2, num):
            if num % i == 0:
                Eprimo =0
                break
        if (Eprimo):
            primo = primo + str(num) + ", "
            cont += 1
            if (cont % 10 == 0):
                primo = primo + "<br>"
        num += 1
    return primos


if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

