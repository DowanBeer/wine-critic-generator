import json
from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/critic")
def critic():
    with open('data.json') as data_file:
            data = json.load(data_file)

    critique = 'ce vin a une magnifique robe {0}, son gout {1} avec sa texture {2} font ressortir ses arômes de {3} c est un magnifique {4}'.format(
                data['qualificatifs']['robes'][randint(0, len(data['qualificatifs']['robes']) - 1)],
                data['qualificatifs']['gouts'][randint(0, len(data['qualificatifs']['gouts']) - 1)],
                data['qualificatifs']['textures'][randint(0, len(data['qualificatifs']['textures']) - 1)],
                data['qualificatifs']['aromes'][randint(0, len(data['qualificatifs']['aromes']) - 1)],
                data['qualificatifs']['cépages'][randint(0, len(data['qualificatifs']['cépages']) - 1)]
            )

    return critique

if __name__ == "__main__":
    app.run()
