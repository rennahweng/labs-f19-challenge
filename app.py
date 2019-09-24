from flask import Flask
import requests 

app = Flask(__name__)

@app.route("/pokemon/<query>")
def pokemon(query):
	api_url = "https://pokeapi.co/api/v2/pokemon/" + 
	r = requests.get(api_url)

    # if the query entered is an id integer
	if(query.isdigit()):
        # displace the pokemon name with its id
		return 'The pokemon with id %s is %s' % (query,r.json()["name"])

    # else if the query entered is a pokemon name string
	else:
        # displace the pokemon id with its name
		return '%s has id %s' % (query,r.json()["id"])
	

if __name__ == '__main__':
   app.run(debug=True)
