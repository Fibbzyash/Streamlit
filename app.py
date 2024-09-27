from flask import Flask , render_template , request , redirect 

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome to the Flask APP!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    return render_template('login.html', email=email, password=password)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return render_template('register.html', name=name, email=email, password=password)




## variable rules
@app.route('/user/<name>')
def user(name):
    return  f"Hello {name}!"

#building url dyanamically
@app.route('/user/<int:score>')
def user_score(score):
    res = "Pass" if score > 50 else "Fail"
    result = {
        "Score": score,
        "Result": res
    }
    return render_template('result1.html', result=result)









if __name__ == '__main__':
    app.run(debug = True , port=5001)  
