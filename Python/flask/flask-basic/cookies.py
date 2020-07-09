from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookies.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    cookie = request.cookies.get('username')
    if cookie is not None:
        return 'Hallo {}'.format(cookie)
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    resp = make_response('Hello {}!'.format(name))
    resp.set_cookie('username', name)
    return resp

if __name__ == "__main__":
    app.run(port=1887,debug=True)