from flask import Flask, render_template, redirect, url_for, request, flash, session, safe_join, send_from_directory
import time
#from flask_caching import Cache
from flask_sessionstore import Session
from subprocess import check_output
import subprocess
import os
from flask_wtf.csrf import CSRFProtect

#secret_key = 'test'
#SECRET_KEY = 'the swauaewriojerwer iorjoijreioajei'
app = Flask(__name__, static_folder='static')

#secret_key = 'test'
#SECRET_KEY = 'the swauaewriojerwer iorjoijreioajei'
#app.secret_key = 'test'
app.config['SECRET_KEY'] = 'test'
app.config['SESSION_TYPE'] = 'filesystem'
#app.config['USE_SIGNER'] = True
#SESSION_USE_SIGNER = True
#SESSION_COOKIE_SECURE=True,
#SESSION_COOKIE_HTTPONLY=True
#SESSION_COOKIE_SAMESITE='Lax'
app.config['SESSION_USE_SIGNER'] = True
#app.config['SESSION_COOKIE_SECURE']=True,
#app.config['SESSION_COOKIE_HTTPONLY']=True
#app.config['SESSION_COOKIE_SAMESITE']='Lax'

#WTF_CSRF_ENABLED = True
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})
sess = Session(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
#sess.init_app(app)


#@app.route('/robots.txt', methods=['POST', 'GET'])
#def static_from_root():
 #   return send_from_directory(app.static_folder, request.path[1:])
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        with open('Login.txt', 'r') as file:
            for line in file:
                userN, passW, twoF = line.strip().split(',')
                if userN == request.form['username']:
                    flash('User already exists please login')
                    return render_template('register.html')
        file.close()
        with open('Login.txt', 'r') as file:
            for line in file:
                userN, passW, twoF = line.strip().split(',')
            if userN != request.form['username'] and twoF == request.form['twoFactor']:
                flash('2fa is in use, are you already registered? Please relogin.')
                return render_template('register.html')

        file.close()
        if not request.form['twoFactor'].isdigit():
            flash('Two-factor failure')
            return render_template('register.html')
        if  not (len(request.form['twoFactor']) < 13):  
            flash('Two-factor failure')
            return render_template('register.html')
        if not (len(request.form['twoFactor']) >= 10):
            flash('Two-factor failure')
            return render_template('register.html')
        with open('Login.txt', 'a') as file:
            #userN, passW, twoF = line.strip().split(',')
            file.write(request.form['username'])
            file.write(',')#\n
            file.write(request.form['password'])
            file.write(',')
            if request.form['twoFactor'] == '':
                file.write('\n')
            else:
                file.write(request.form['twoFactor'])
                file.write('\n')
            file.close()
            flash('Registered successfully, Please Login')      

    return render_template('register.html')


    #return "Hello World!"
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
                        if twoF == '':
                            flash('Logged in successfully')     
                            return render_template('login.html')
                        if twoF == request.form['twoFactor']:
                            flash('Logged in successfully')
                            #isauthenticated = True
                            session['auth'] = True
                            return render_template('login.html')
                            #return redirect(url_for('spell_check'))
                        elif twoF != request.form['twoFactor']:
                            flash('Two-factor failure')
                            session['auth'] = False
                            return render_template('login.html')
        if not ((userN == request.form['username']) and (passW == request.form['password'])):
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
    #dictionary = "/templates/asd.txt"
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
        #return '{} {} {} {} {} {} {}'.format(misspelled, seperator, process, seperator, thewords, seperator, words)
        return render_template('spell_check.html',bruhthemisspelledwords=process, bruhtheinput=words)
    return render_template('spell_check.html')

    #misspelledOut = process.replace("\n", ", ").strip().strip(',')
#       misspelledOut = [x for x in pattern.split(process) if x]
    
@app.route('/success')
def flash_success():
    flash('This message will be visible!')
    time.sleep(1)
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
