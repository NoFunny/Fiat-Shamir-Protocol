from flask import Flask, render_template
from TrustedСenter import TrustedCenter
from User import User
from FiarShamirProtocol import FiatShamirProtocol

app = Flask(__name__)

tc = TrustedCenter()
usrA = User()
usrB = User()
usrEva = User()


@app.route('/')
def index():
    global tc, usrA, usrB, usrEva
    tc = TrustedCenter()
    usrA = User()
    usrB = User()
    usrEva = User()
    return render_template('index.html')


@app.route("/createUserA/", methods=['GET'])
def createUserA():
    global usrA, tc
    usrA = User.initUserA(User(), tc.n)
    print('OK')
    return render_template('index.html')


@app.route("/createUserB/", methods=['GET'])
def createUserB():
    global usrB, tc
    usrB = User.initUserB(User())
    print('OK')
    return render_template('index.html')


@app.route("/createEva/", methods=['GET'])
def createEva():
    global usrA ,usrEva, tc
    usrEva = User.initEva(User(), tc.n)
    usrA = usrEva
    print('OK')
    return render_template('index.html')


@app.route("/500/")
def errorStatus():
    return render_template('500.html')


@app.route("/success/")
def okStatus():
    return render_template('success.html')


@app.route("/startProtocol/<rounds>/", methods=['GET', 'POST'])
def startProtocol(rounds):
    print("Rounds = ", rounds)
    global usrA, usrB, usrEva, tc
    fsp = FiatShamirProtocol(tc, usrA, usrB)
    if fsp.start(int(rounds)):
        return render_template('success.html')
    else:
        return render_template('500.html')


if __name__ == '__main__':
    app.run(debug=True)
