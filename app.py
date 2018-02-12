from flask import Flask

app=Flask(__name__) #creating obj of flask using a unique name

#decorator
@app.route('/')  #creating route which is for home page of our app eg. for google..it can be http://google.com/ or / maps for specific page
def home():
    return "Hello, world!"

app.run(port=5000)

#here our app returns data Hello,world