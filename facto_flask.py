from flask import Flask, jsonify

app = Flask(__name__)
#Guia
@app.route('/')
def home():
    return "Usa en la barra de direcciones /fact/[numero que quieres factorizar] para calcular el factorial"

@app.route('/fact/<int:fact>')
def factorial(fact):
    # factorial
    resultado = 1
    for i in range(1, fact + 1):
        resultado *= i
    
    #  factorial es par o impar
    etiqueta = "par" if resultado % 2 == 0 else "impar"
    
    #  JSON
    respuesta = {
        "numero": fact,
        "factorial": resultado,
        "tipo": etiqueta
    }
    
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
