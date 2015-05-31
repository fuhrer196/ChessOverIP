import socket
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

delay = 0.0055

SA1 =
SA2 =
SB1 =
SB2 =
TA1 =
TA2 =
TB1 =
TB2 =

GPIO.setup(SA1,GPIO.OUT)
GPIO.setup(SA2,GPIO.OUT)
GPIO.setup(SB1,GPIO.OUT)
GPIO.setup(SB2,GPIO.OUT)
GPIO.setup(TA1,GPIO.OUT)
GPIO.setup(TA2,GPIO.OUT)
GPIO.setup(TB1,GPIO.OUT)
GPIO.setup(TB2,GPIO.OUT)

def setStepS(w1,w2,w3,w4):
    GPIO.output(SA1,w1)
    GPIO.output(SA2,w2)
    GPIO.output(SB1,w3)
    GPIO.output(SB2,w4)

def moveforwardS(steps):
    for i in range(steps):
        setStepS(1,0,0,0)
        time.sleep(delay)
        setStepS(0,0,1,0)
        time.sleep(delay)
        setStepS(0,1,0,0)
        time.sleep(delay)
        setStepS(0,0,0,1)
        time.sleep(delay)

def movebackwardS(steps):
    for i in range(steps):
        setStepS(0,0,0,1)
        time.sleep(delay)
        setStepS(0,1,0,0)
        time.sleep(delay)
        setStepS(0,0,1,0)
        time.sleep(delay)
        setStepS(1,0,0,0)
        time.sleep(delay)

def setStepT(w1,w2,w3,w4):
    GPIO.output(TA1,w1)
    GPIO.output(TA2,w2)
    GPIO.output(TB1,w3)
    GPIO.output(TB2,w4)

def moveforwardT(steps):
    for i in range(steps):
        setStepT(1,0,0,0)
        time.sleep(delay)
        setStepT(0,0,1,0)
        time.sleep(delay)
        setStepT(0,1,0,0)
        time.sleep(delay)
        setStepT(0,0,0,1)
        time.sleep(delay)

def movebackwardT(steps):
    for i in range(steps):
        setStepT(0,0,0,1)
        time.sleep(delay)
        setStepT(0,1,0,0)
        time.sleep(delay)
        setStepT(0,0,1,0)
        time.sleep(delay)
        setStepT(1,0,0,0)
        time.sleep(delay)

def Main():
    socket = socket.socket()
    host = '0.0.0.0'
    port = 5001
    socket.bind((host,port))
    socket.listen(10)
    c, addr = socket.accept()

    while 1:
        c.send("StepsS:")
        stepsS = c.recv(1024)
        c.send("StepsT:")
        stepsT = c.recv(1024)
        if stepS > 0:
            moveforwardS(stepsS)
        else:
            movebackwardS(-stepsS)
        if stepsT > 0:
            moveforwardT(stepsT)
        else:
            movebackwardT(stepsT)
                
        
if __name__ == '__main__':
    Main()
