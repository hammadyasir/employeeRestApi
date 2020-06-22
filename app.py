# from flask import Flask
#
# from flask_restful import Resource, Api
#
#
# app = Flask(__name__)
# api = Api(app)
# employee_info = {
#     "emp1":{
#         "name":"xyz",
#         "salary":"10L",
#
#     },
#     "emp2":{
#         "name":"abc",
#         "salary":"14L",
#     },
# }
#
# class Employee(Resource):
#     def get(self):
#         return employee_info
#
#
# api.add_resource(Employee,"/info")
#
#
#
#
# app.run(port=5000,host="localhost")




from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)



# /
# /ping
# info

class Help(Resource):
    def get(self):
        help = {
            "Available REST API are":["/ping","/info"]
        }
        return help


class Ping(Resource):
    def get(self):
        status={
            "status":"Alive"
        }
        return status


class Employee(Resource):
    def get(self):
        employee_info={
            "emp1":{
                "name":"xyz",
                "salary":"10L"
            },
            "emp2":{
                "name":"mnq",
                "salary":"20L"
            }
        }
        return employee_info



# now we need to add the resource (datae) to the Api

api.add_resource(Help, "/")
api.add_resource(Ping, "/ping")
api.add_resource(Employee, "/info")



# to run the application

# app.run(host='localhost', port=5000, debug=True)
app.run(port=5000, host='localhost')
