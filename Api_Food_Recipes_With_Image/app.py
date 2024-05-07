from flask import Flask, render_template, request
from key import api_key
import requests
from googletrans import Translator


app = Flask(__name__)

@app.route('/')
def  web_simple():
   
    return render_template('index.html')

@app.route('/busca', methods=['GET', 'POST'])
def web_simple_busca():
    translator = Translator()
    if request.method == 'POST':

        # obtendo a busca do html
        query_pt = request.form['search']
        query_en = translator.translate(query_pt, dest='en')
        query = query_en.text
        
        
        # url e o input
        url = "https://food-recipes-with-images.p.rapidapi.com/"
        querystring = {"q": query}

        # headers
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "food-recipes-with-images.p.rapidapi.com"
        }

        # requisição
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            recipes = response.json()['d']
        else:
            recipes = []

        recipes_formatted = []
        for recipe in recipes:
            formatted_recipe = {
                'Title' : recipe['Title'],
                'Ingredients' : recipe['Ingredients'],
                'Instructions' : recipe['Instructions'],
                'Image' : recipe['Image']
            }
            recipes_formatted.append(formatted_recipe)


        return render_template('busca.html', recipes=recipes_formatted)
    else:
        return render_template('busca.html')



if __name__ == '__main__':
    app.run()