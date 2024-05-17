from flask import Flask, render_template, request
from key import api_key, USER, PASS
import requests
from googletrans import Translator
import oracledb

dsn = oracledb.makedsn('oracle.fiap.com.br', 1521, service_name='ORCL')
connection = oracledb.connect(user=USER, password=PASS, dsn=dsn)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def web_simple_busca():
    recipe_limit = 5
    recipe_count = 0 
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
            translated_ingredients = recipe['Ingredients']
            for index in recipe['Ingredients'].keys():                
                translated_ingredients[index] = translator.translate(recipe['Ingredients'][index], dest='pt').text
            
            formatted_recipe = {
                'Title' : translator.translate(recipe['Title'], dest='pt').text,                
                'Ingredients' : translated_ingredients,
                'Instructions' : translator.translate(recipe['Instructions'], dest='pt').text,
                'Image' : recipe['Image']
            }
            recipes_formatted.append(formatted_recipe)
            recipe_count += 1
            if recipe_count >= recipe_limit:
                break


        return render_template('busca.html', recipes=recipes_formatted)
    else:
        return render_template('busca.html')



if __name__ == '__main__':
    app.run()