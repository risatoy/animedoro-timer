from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        study = int(request.form['study'])
        rest = int(request.form['rest'])
        sets = int(request.form['sets'])

        session['study'] = study * 60
        session['rest'] = rest * 60
        session['sets'] = sets
        session['set_counter'] = 0

        return redirect(url_for('study'))

    return render_template('index.html')

@app.route('/study')
def study():
    if session['set_counter'] == session['sets']:
        return redirect(url_for('completed'))

    session['set_counter'] += 1
    return render_template('study.html', study=session['study'], sets=session['set_counter'])

@app.route('/break')
def rest():
    return render_template('break.html', rest=session['rest'], sets=session['set_counter'])

@app.route('/complete')
def completed():
    return render_template('complete.html', sets=session['set_counter'])


if __name__ == '__main__':
    app.run(port=5000)