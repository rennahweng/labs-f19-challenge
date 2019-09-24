from flask import Flask
import requests 

app = Flask(__name__)

@app.route("/pokemon/<query>")
def pokemon(query):
    # use request library to get API
	# have the API URL as a place holder so the query won't become a string
	api_url = "https://pokeapi.co/api/v2/pokemon/" + query
    # r returns the pokemon information from PokeAPI
	r = requests.get(api_url)

    # distinguish between name query and id query by
    # checking if it is a string or an 
	if (isinstance(query, str)):
		return 'The pokemon with id %s is %s' % (query,r.json()["name"]) #extract the key named "name"

	else if (query.isdigit()):
		return '%s has id %s' % (query,r.json()["id"]) #extract the key named "id" from each pokemon's 
	
	else:
		return 'ERROR! Please enter in a valid pokemon id or name.' #error message if use input is incorrect

if __name__ == '__main__':
   app.run(debug=True)
