from flask import Flask, request, make_response, render_template, redirect, url_for, session

app = Flask(__name__, template_folder="templates")
app.secret_key = 'SOME KEY'



@app.route('/')
def index():
    return render_template(template_name_or_list = 'index.html', message = 'Index')

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    return render_template('index.html', message= 'Session data set')


@app.route('/get_data')
def get_data():
    name = session['name']
    other = session['other']
    return render_template(template_name_or_list = 'index.html', message = f"Name: {name}, Other: {other}")


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template(template_name_or_list = 'index.html', message = "Session Data Cleared")

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template(template_name_or_list = 'index.html', message = "Cookie set."))
    response.set_cookie(key =  'cookie_name', value = 'cookie_value' )
    return response


@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template(template_name_or_list = 'index.html', message = f'Cookie Value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template(template_name_or_list = 'index.html', message = "Cookie Removed"))
    response.set_cookie(key =  'cookie_name', expires = 0 )
    return response


# @app.route('/')
# def index():
#     value = "Flask Application"
#     result = [10, 20, 30, 40, 50]
#     return render_template('index.html', myValue = value, myResult = result);

# @app.route("/other")
# def other():
#     some_text = "Hello, World"
#     return render_template('index.html', some_text = some_text);

@app.route('/form-route', methods=['GET', 'POST'])
def routes():
    if request.method == 'GET':
        return render_template('index.html') 
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'saketh' and password == 'password':
            return 'Success'
        else:
            return 'Failure'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    return ""

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('revers_string')
def revers_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times = 2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

@app.route("/hello", methods=['GET','POST'])
def hello():
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response;
    
    # if request.method == "GET":
    #     return 'You made a GET request\n', 200
    # elif request.method == "POST":
    #     return "You made a POST request\n", 200
    # else:
    #     return "You will never see this message\n", 404

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"

@app.route("/handle_url_params")
def handle_params():
    greeting = request.args['greeting']
    name = request.args.get('name')
    return f"{greeting}, {name}"


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5555, debug = True)