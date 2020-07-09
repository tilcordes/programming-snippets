from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('get_and_post.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    name = ''
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    return 'Hello {}!'.format(name)

if __name__ == "__main__":
    app.run(port=1887, debug=True)