from flask import Flask, request, render_template, escape, session, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(request.url)
    else:
        if 'name' in session:
            return 'Hello {}'.format(escape(session['name']))
        else:
            return render_template('sessions.html')

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect(url_for('index'))


app.secret_key = '\xc8\x85\xe1\xfdB\xe5\xcf[\xaf\xcb\x9d\xf7\x9f@E\xf0\xb3\xbd\xe1b\xe4%#\xfa'

if __name__ == "__main__":
    app.run(port=1887, debug=True)