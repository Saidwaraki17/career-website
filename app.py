from flask import Flask, render_template, jsonify, request

from database import load_jobs_from_db, load_job_from_db, add_application_to_db

from sqlalchemy import text

# Flask is framework for web technologies
# we are creating an app which is an object in python

# so we create a object in python named app

app = Flask(__name__)

# __name__ returns __main__ function
'''
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
'''

# next we add a @oject.route(host = 'address', debug = 'True') method to object where the url triggered to other page


@app.route("/")  # this is empty page
def hello_world():
  list_of_jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs=list_of_jobs,
                         company_name="EBAIEE FUTRUZ")


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found!", 404
  return render_template('jobpage.html', job=job)

@app.route('/job/<id>/apply',methods = ['post'])
def apply_to_job():
  data = request.form
  job = load_job_from_db(id)

  add_application_to_db(id,data)
  # this stores data and email
  return render_template('application_submitted.html', application = data, job = job)
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)  # we need to give a host address
# if we add 0.0.0.0 it runs in local environent

# Flask and gunicorn-- a development based server which is not used for production ,are added into requirements.txt which is standard file for build command at render.

# To put a Flask application into production we need gunicorn library.
