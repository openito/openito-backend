import json
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)



class Hello(Resource):
    def get(self):
        return {'message': 'Hello World!'}

    def post(self):
        data = request.args.copy()
        print('RECEIVED DATA:', data)
        data['success'] = True
        return data
api.add_resource(Hello, '/')


#gets event and adds it to the file
class JSONStuff(Resource):
    def get(self):
        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
        print('RECEIVED DATA:', data)
        #self.post()    #testing
        return data

    def post(self):
        #event_to_add = json.loads(request.data) #data from current interaction
        with open("data_file.json", "r") as read_file:
            json_data = json.load(read_file)
            event_to_add = json.loads("""
            {
                "title": "Midnight Coding Session with Bob",
                "date": 837479837459,
                "location": {
                    "latitude": 64.2008,
                    "longitude": 149.4937
                },
                "numberAttending": 1
            }
            """)
            json_data["events"].append(event_to_add)

            with open("data_file.json", "w") as write_file:
                json.dump(json_data, write_file)
        return json_data

api.add_resource(JSONStuff, '/JSONStuff')







if __name__ == '__main__':
    app.run(debug=True)
