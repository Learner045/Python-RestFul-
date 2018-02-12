from flask import Flask
from flask_restful import Resource,Api


flaskrestfulapp=Flask(__name__)
api=Api(flaskrestfulapp)


#a resource can be thought of as an entity here Student
class Student(Resource):
    def get(self,name):  #making a GET REQ
        return {'student':name}

                            #here we are providing route similar to app.route('/student/<string:name>') but not using a decorator for it
api.add_resource(Student, '/student/<string:name>')  #http://127.0.0.1:5000/student/rolf

flaskrestfulapp.run(port=5000)