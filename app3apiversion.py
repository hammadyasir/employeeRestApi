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
            "All Endpoints":["/api/v1/esinfo","/api/v1/esinfo/:ename"]
        }
        return help







class Employees(Resource):
    def get(self, ename=None):
        if ename:
            if ename in employee_info.keys():
                return employee_info.get(ename)
            else:
                message={
                    "message":"sorry is not found in my list"
                }
                return message
        else:
            return employee_info




api.add_resource(Help,"/")
api.add_resource(Employees,"/api/v1/esinfo","/api/v1/esinfo/<string:ename>")



app.run(debug=True,port=5000,host="localhost")
