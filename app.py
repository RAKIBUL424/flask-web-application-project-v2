from flask import (
Flask,
render_template,
jsonify
)

app= Flask(__name__)

JOBS= [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bangaluru',
    'salary': 'TK 45000'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'San Francisco, USA',
    
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Dhaka',
    'salary': 'TK 55000'
  },
  {
    'id': 4,
    'title': 'Data Scientst',
    'location': 'Remote',
    'salary': 'TK 85000'
  },
]


@app.route("/")
def home():
  return render_template("home.html", jobs=JOBS,
                        company_name="Gwen IT")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)



if __name__ == "__main__":
  app.run(host= "0.0.0.0", debug=True)