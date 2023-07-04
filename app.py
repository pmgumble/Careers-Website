from flask import Flask, render_template

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'SA, USA',
    'salary': '$110,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
