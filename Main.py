import subprocess
import Rpi.GPI as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)
GPIO.setup(14,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(26,GPIO.IN)
GPIO.setup(12,GPIO.IN)
pwm1=GPIO.PWM(18,50)
pwm2=GPIO.PWM(23,50)
pwm3=GPIO.PWM(24,50)
pwm4=GPIO.PWM(25,50)
pwm5=GPIO.PWM(17,50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm5.start(0)
wifite_scan = subprocess.Popen('node webserver.js', shell=True, stdout=subprocess.PIPE)
while True:
    output = wifite_scan.stdout.readline()
    if output == '':
        # end of stream
        print("End of Stream")
        break
    if output is not None:
        # here you could do whatever you want with the output.
        print("Output Read: "+output)
    
