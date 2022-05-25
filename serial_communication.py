import subprocess
import time
import serial
wifite_scan = subprocess.Popen('node webserver.js', shell=True, stdout=subprocess.PIPE)
ser = serial.Serial('/dev/ttyACM0',115200, timeout=1)
ser.flush()

while True:
    print ("code begins")
    time.sleep(1)
    textdata = "I am Pi"
    ser.write(textdata.encode('utf-8'))
    line = ser.readline().decode('utf-8').rstrip()
    print (line)
    time.sleep(1)
    output = wifite_scan.stdout.readline().decode('utf-8')
    time.sleep(1)
    print (output)
    print ("The above numerical data is from Web Server")
    stroutput = str(output)
    print stroutput
    print "The above is String cnverted output"
    
    print stroutput
    print "The above is newline appended string output"
    ser.write(stroutput.encode('utf-8'))
    print "I am line2"
    line2 = ser.readline().decode('utf-8').rstrip()
    print (line2)
    time.sleep(1)
    print "code ends"
#    output = wifite_scan.stdout.readline().encode('utf-8')
#    if output == '':
        # end of stream
#        print("End of Stream")
#        break
#    if output is not None:
        # here you could do whatever you want with the output.
#        print("Output Read: "+output)
#        ser.write(b"%s"%output)
        
        
