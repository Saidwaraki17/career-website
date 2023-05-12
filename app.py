from flask import Flask ,render_template, jsonify

# Flask is framework for web technologies
# we are creating an app which is an object in python

# so we create a object in python named app

app = Flask(__name__) 

# __name__ returns __main__ function

JOBS = [
  {
  'id' : 1,
  'Title' : "Data Analyst",
  'Location' : 'Bengaluru, India',
  'Salary' : 'Rs.1,30,000'
  },
  {
      'id' : 2,
  'Title' : "Data Scientist",
  'Location' : 'Hyderabad, India',
  'Salary' : 'Rs.2,50,000'
  },
   {
      'id' : 3,
  'Title' : "Front-end Engineer",
  'Location' : 'Delhi, India',
  'Salary' : 'Rs.2,00,000'
  },
  {
      'id' : 4,
  'Title' : "Back-end Engineer",
  'Location' : 'Kochi, India',
  'Salary' : 'Rs.2,50,000'
  },
  {
      'id' : 5,
  'Title' : "ML Engineer",
  'Location' : 'San Fransisco, USA',
  'Salary' : 'US $150,000'
  },
]


# next we add a @oject.route(host = 'address', debug = 'True') method to object where the url triggered to other page

@app.route("/") # this is empty page 
def hello_world():
  return render_template('home.html', 
                         jobs = JOBS,
                        company_name = "Eplain")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True) # we need to give a host address 
# if we add 0.0.0.0 it runs in local environent 



