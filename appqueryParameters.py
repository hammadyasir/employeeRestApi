from flask import  Flask,request
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
            "All Endpoints":["/esinfo"]
        }
        return help

class Employees(Resource):
    def get(self):
        if request.args:
            emp_name=request.args.get("ename")
            if emp_name in employee_info.keys():
                return employee_info.get(emp_name)
            message={
                "message":"sorry !!! we do not find given emp name in our list"
            }
            return message

        return employee_info



    # print(request.args.get("ename"))


api.add_resource(Help,"/")
api.add_resource(Employees,"/esinfo")



app.run(debug=True,port=5000,host="localhost")
