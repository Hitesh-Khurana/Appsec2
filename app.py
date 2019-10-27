from flask import Flask, render_template, redirect, url_for, request, flash, session, safe_join
import time
#from flask_caching import Cache
from flask_sessionstore import Session
from subprocess import check_output
import subprocess
import os

app = Flask(__name__)

app.secret_key = 'test'
app.config['SESSION_TYPE'] = 'filesystem'
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})
sessionstore = Session(app)
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/login', methods=['POST', 'GET'])
# @cache.cached(timeout=0)
def login():
    # error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            flash('Username or Password is invalid.')
        else:
            flash('Logged in successfully, Redirecting')
            return redirect(url_for('spell_check'))
    return render_template('login.html')


@app.route('/spell_check', methods=['POST', 'GET'])
def spell_check():
    dictionary = "/templates/asd.txt"
    if request.method == 'POST':
        words = request.form['word']
        misspelled = 'misspelled-words: '
        seperator = '|'
        thewords = 'Original Input: '
        with open('output-words.txt', 'w') as f:
            f.write(str(words))
            f.close()
        #stdout = subprocess.check_output(["./templates/some.sh", words, dictionary])#.decode('utf-8')
        process = subprocess.check_output(['./a.out', 'output-words.txt', "wordlist.txt"]).decode('utf-8').rstrip()
        return '{} {} {} {} {} {} {}'.format(misspelled, seperator, process, seperator, thewords, seperator, words)
    return render_template('spell_check.html')


@app.route('/success')
def flash_success():
    flash('This message will be visible!')
    time.sleep(1)
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)
