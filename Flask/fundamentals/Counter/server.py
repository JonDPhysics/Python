from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ='keep it secret, keep it safe'

@app.route('/')
def start():
    if 'count' in session: 
        session['count'] = session['count'] + 1
        return render_template('index.html')
    else:
        session['count'] = 1
    return render_template('index.html')

@app.route("/addTwo")
def addTwo():
    session['count'] = session['count'] + 2
    return render_template('index.html')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)