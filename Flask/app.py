from flask import Flask,render_template,request,jsonify

# Create a Flask application instance
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello, Flask!"

@app.route('/index',methods=['GET'])
def index():
    return "Index Page"

## Variable rule:
@app.route('/success/<int:score>')
def success(score):
    return f"Your score is {score}"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form.get('name')
        age = request.form.get('age')
        return f"Name: {name}, Age: {age}"



## how to create api
@app.route("/api", methods=['POST'])
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify( a_val + b_val)

if __name__ == '__main__':
   app.run(debug=True)
