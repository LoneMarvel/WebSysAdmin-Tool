#!/usr/bin/python3.6

from flask import Flask, render_template
from sys import platform
import subprocess

app = Flask(__name__)

def cmdExec(cmdString):
    sysOut = subprocess.getoutput(cmdString)
    return sysOut


@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/diskSpace')
def DisplayDiskSpace():
    cmdOut = cmdExec('df -h')
    return render_template('diskSpace.html', cmdOut=cmdOut)


@app.route('/freemem')
def DisplayMem():
    if ( platform == 'darwin' ):
        cmdOut = cmdExec('top -l 1 | grep Phy')
    elif ( platform == 'linux' ):
        cmdOut = cmdExec('free -mh')
    else:
        cmdOut = 'Sorry Not Available For Windows'

    return render_template('freemem.html', cmdOut=cmdOut)


@app.route('/netinfo')
def NetInfo():
    if ( platform == 'darwin' ):
        cmdOut = cmdExec('bash mac-netinfo')
    elif ( platform == 'linux' ):
        cmdOut = cmdExec('./netinfo')
    else:
        cmdOut = 'Sorry Not Available For Windows'

    return render_template('netinfo.html', cmdOut=cmdOut)


@app.route('/ping')
def Ping():
    cmdOut = cmdExec('ping -c 3 8.8.8.8')
    return render_template('ping.html', cmdOut=cmdOut)

@app.route('/runprocess')
def runningProcess():
    myFilter = 'chrome'
    cmdOut = cmdExec('top -b -n 1 | grep -i '+myFilter)
    return render_template('runprocess.html', cmdOut=cmdOut)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')