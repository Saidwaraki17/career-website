from flask import Flask

# Flask is framework for web technologies
# we are creating an app which is an object in python

# so we create a object in python named app

app = Flask(__name__) 

# __name__ returns __main__ function

# next we add a @oject.route(host = 'address', debug = 'True') method to object where the url triggered to other page

@app.route("/") # this is empty page 
def hello_world():
  return "Hello World!"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True) # we need to give a host address 
# if we add 0.0.0.0 it runs in local environent 



