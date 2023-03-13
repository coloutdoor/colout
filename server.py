from flask import Flask,json

print ("I am the server")

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
project = [{"id": 99, "name": "MyProject"}, "type", "Deck"]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/project/new', methods=['POST'])
def new_project():
   return json.dumps(project)
if __name__ == '__main__':
    api.run()