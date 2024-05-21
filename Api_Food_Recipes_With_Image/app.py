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
    translator = Translator()

    if request.method == 'POST':
        # obtendo a busca do html
        query_pt = request.form['search']
        query_en = translator.translate(query_pt, dest='en')
        query = query_en.text

        #salvando a busca no Banco de dados
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO T_API_RECEITAS(cod_pesquisa, nm_pesquisado) VALUES(SEQ_API_RECEITAS.nextval, :1)"
            cursor.execute(sql, [query_pt])
            connection.commit()
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"An error occurred: {error.code} - {error.message}")
        finally:
            cursor.close()        
        
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
            recipes = response.json()['d'][:3]
        else:
            recipes = []

        recipes_formatted = []
        for recipe in recipes:
            translated_ingredients = []
            for ingredient in recipe['Ingredients'].values():
                translated_ingredient = translator.translate(ingredient, dest='pt').text
                translated_ingredients.append(translated_ingredient)
            
            formatted_recipe = {
                'Title': translator.translate(recipe['Title'], dest='pt').text,
                'Ingredients': translated_ingredients,
                'Instructions': translator.translate(recipe['Instructions'], dest='pt').text,
                'Image': recipe['Image']
            }
            recipes_formatted.append(formatted_recipe)

        return render_template('busca.html', recipes=recipes_formatted)
    else:
        return render_template('busca.html')

if __name__ == '__main__':
    app.run()
