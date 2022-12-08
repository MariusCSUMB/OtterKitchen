from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

my_key = 'd53b43f7d9d14401a56568b6af67fe2e'

endpoint1 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}'

endpoint2 = f'https://api.spoonacular.com/food/trivia/random?apiKey={my_key}'

endpoint3 = f'https://api.spoonacular.com/food/jokes/random?apiKey={my_key}'

'''foodFacts = []
for i in range(3):
    req = requests.get(endpoint2)
    data = req.json()
    singleFact = data.get("text")
    foodFacts.append(singleFact)'''



@app.route("/")
def main():
    foodFacts = []

    for i in range(3):
        req = requests.get(endpoint2)
        data = req.json()
        singleFact = data.get('text')
        foodFacts.append(singleFact)
    
    jokesList = []
    for i in range(3):
        req2 = requests.get(endpoint3)
        data = req2.json()
        singleJoke =  data.get('text')
        jokesList.append(singleJoke)

    return render_template("frontpage.html", foodFacts = foodFacts, jokesList=jokesList)


@app.route("/random")
def index():
    try:
        r = requests.get(endpoint1)
        data = r.json()
        print(data)
    except:
        print('please try again')
    return render_template("random.html", data = data)


endpoint1 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&tags=vegetarian&instructionsRequired=true'
@app.route("/vegetarian")
def veggie():
    try:
        r = requests.get(endpoint1)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("vegetarian.html", data = data)

endpoint1 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=breakfast&instructionsRequired=true'
@app.route("/breakfast")
def breakfast():
    try:
        r = requests.get(endpoint1)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("breakfast.html", data = data)

endpoint = f'https://api.spoonacular.com/recipes/autocomplete?number=4&query=sandwhich&apiKey={my_key}'
@app.route("/sandwhich")
def sandwhich():
    try:
        r = requests.get(endpoint)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("sandwhich.html", data = data)


endpoint3 = f'https://api.spoonacular.com/recipes/random?apiKey={my_key}&number=3&type=vegan&instructionsRequired=true'
@app.route("/vegan")
def vegan():
    try:
        r = requests.get(endpoint3)
        data = r.json()
        # print(data)
    except:
        print('please try again')
    return render_template("vegan.html", data = data)