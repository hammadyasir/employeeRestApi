from flask import  Flask
from flask_restful import Resource, Api


app=Flask(__name__)
api=Api(app)

employee_info={
    "john":{
        "salary":"10L",
        "Technology":"Linux Admin",

    },
    "kelly":{
        "salary":"1000$",
        "Technology":"Web Developer",

    },
}

class Help(Resource):
    def get(self):
        help={
            "All Endpoints":["/esinfo","/einfo/:ename"]
        }
        return help




class Employees(Resource):
    def get(self):
        return employee_info


class Employee(Resource):
    def get(self,ename):
        return employee_info.get(ename)


api.add_resource(Help,"/")
api.add_resource(Employees,"/esinfo")
api.add_resource(Employee,"/einfo/<string:ename>")



app.run(port=5000,host="localhost",debug=True)
