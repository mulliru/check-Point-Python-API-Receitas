from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def  web_simple():
   
    return render_template('index.html')

@app.route('/busca', methods=['GET', 'POST'])
def web_simple_busca():
    if request.method == 'POST':
        # obtendo a busca do html
        query = request.form['search']
        
        # url e o input
        url = "https://food-recipes-with-images.p.rapidapi.com/"
        querystring = {"q": query}

        # headers
        headers = {
            "X-RapidAPI-Key": "ea262b61c3msh5f9d62d6beadb81p1efeb9jsne5e93e8bdc7a",
            "X-RapidAPI-Host": "food-recipes-with-images.p.rapidapi.com"
        }

        # requisição
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            recipes = response.json()['d']
        else:
            recipes = []

        def format_recipe_info(recipe):
            title = recipe['Title']
            ingredients = recipe['Ingredients']
            instructions = recipe['Instructions']
            image = recipe['Image']
            
            formatted_info = f"Título: {title}\n\nIngredientes:\n"
            for key, value in ingredients.items():
                formatted_info += f"{key}. {value}\n"
            
            formatted_info += f"\nInstruções:\n{instructions}\n\nImagem: {image}\n\n---"
            
            return formatted_info

        recipes_formatted = [format_recipe_info(recipe) for recipe in recipes]

        return render_template('busca.html', recipes=recipes_formatted)
    else:
        return render_template('busca.html')



if __name__ == '__main__':
    app.run()