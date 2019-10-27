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
 #file = open("Login.txt","a")
  #  file.write (username)
   # file.write (",")
    #file.write (password)
    #file.write("\n")
    #file.close()

@app.route('/login', methods=['POST', 'GET'])
# @cache.cached(timeout=0)
def login():
    # error = None
    #isauthenticated = False
    if request.method == 'POST':
        with open('Login.txt', 'r') as file:
            for line in file:
                userN, passW, twoF = line.strip().split(',')
            #   print("", userN,passW,twoF)
            #   print("", request.form['username'],request.form['password'],request.form['twoFactor'])
                if userN == request.form['username']:
                    if passW == request.form['password']:
                        if twoF == request.form['twoFactor']:
                            flash('Logged in successfully, Redirecting')
                            #isauthenticated = True
                            session['auth'] = True
                            return redirect(url_for('spell_check'))
                        elif twoF != request.form['twoFactor']:
                            flash('Two-factor failure')
                            session['auth'] = False
                elif userN != request.form['username'] or passW != request.form['password']:
                    flash('Incorrect')
                    session['auth'] = False
    return render_template('login.html')


@app.route('/spell_check', methods=['POST', 'GET'])
def spell_check():
    my_var = session.get('auth')
    if my_var == True:
        session['auth'] = True
    elif my_var != True: 
        return redirect(url_for('login'))
    dictionary = "/templates/asd.txt"
    if request.method == 'POST':
        words = request.form['word']
        misspelled = 'misspelled-words: '
        seperator = '|'
        thewords = 'Original Input: '
        with open('output-words.txt', 'w') as f:#pattern = ,
            f.write(str(words))
            f.close()
#stdout = subprocess.check_output(["./templates/some.sh", words, dictionary])#.decode('utf-8')
        process = subprocess.check_output(['./a.out', 'output-words.txt', "wordlist.txt"]).decode('utf-8').replace("\n",", ").rstrip(", ")#[:-2] 
        return '{} {} {} {} {} {} {}'.format(misspelled, seperator, process, seperator, thewords, seperator, words)
    return render_template('spell_check.html')

    #misspelledOut = process.replace("\n", ", ").strip().strip(',')
#       misspelledOut = [x for x in pattern.split(process) if x]
    
@app.route('/success')
def flash_success():
    flash('This message will be visible!')
    time.sleep(1)
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)
