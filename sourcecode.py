[b'import time, socket, datetime, os, fcntl, struct, sqlite3\t#import time, IP, time and date', b'from flask import Flask, render_template, request, jsonify, request, send_file #import web app', b'from w1thermsensor import W1ThermSensor', b'import netifaces as ni', b'#from weather import Weather, Unit', b'', b'#weather = Weather(unit=Unit.CELSIUS)', b'#lookup = weather.lookup(560743)', b'', b'global int_time', b'int_time = datetime.datetime.now()', b'', b'app = Flask(__name__) #Assigns app', b'', b'#os.system("sudo mount -t exfat /dev/sda1 /media/usb")', b'', b'localtime = time.asctime( time.localtime(time.time()) ) #Gets the time', b'print (" * Current time :" + str(localtime)) #Displays Time', b'', b"ni.ifaddresses('eth0')", b"IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']", b'', b'def accessed():', b'\tF = open("A.txt", "r")', b'\tA = F.read()', b'\tF.close()', b'\tF = open("A.txt", "w")', b'\tF.write(str(int(A)+1))', b'\tF.close()', b'', b'', b'def getTemperature():', b'\tsensor = W1ThermSensor()', b'\ttemperature = sensor.get_temperature()', b'\t#temperature = 125.29', b'\treturn(temperature)', b'', b'def makeWebpage():', b'\t#weather = Weather(unit=Unit.CELSIUS)', b'\t#lookup = weather.lookup(17044)', b'\t#wind = lookup.wind', b'\tW = open("templates/index.html", "w")', b'\tF = open("First.txt", "r")', b'\tM = open("Middle.txt", "r")', b'\tL = open("Last.txt", "r")', b'\tT = getTemperature()', b'\tif  T >= 30:', b'\t\tB = "Hot.png"', b'\telif 18 <= T < 30:', b'\t\tB = "Warm.png"', b'\telif 5 < T < 18:', b'\t\tB = "Cold.png"', b'\telif 0 < T <= 5:', b'\t\tB = "rCold.png"', b'\telse:', b'\t\tB = "sCold.png"', b'\tW.write(F.read() + B + M.read() + str(round(T, 1)) + "\xc2\xb0C <h4> " +  str(round(T, 2)) + "\xc2\xb0C </h4> " + L.read())', b'\taccessed()', b'\tW.close()', b'\tF.close()', b'\tM.close()', b'\tL.close()', b'', b"@app.route('/') #Sets index", b'def index():', b'\tmakeWebpage()', b"\treturn render_template('index.html') #Displays HTML page 'Relay.html'", b'\t', b"@app.route('/about') #Sets index", b'def about():', b'\tAf = open("aF.txt", "r")', b'\tAl = open("aL.txt", "r")', b'\tAw = open("templates/about.html", "w")', b'\tN = open("A.txt", "r")', b'\tUptime = datetime.datetime.now() - int_time', b'\tAw.write(Af.read() + "<p> <center> This Weather Station Has Been Used " + str(N.read()) + " Times </center> </p> <p> <center> Temperature (Up to 3dp): " + str(getTemperature()) + "\xc2\xb0C </center> </p> <center> <p> Uptime: " + str(Uptime.days)+ " day(s), " + str(Uptime.seconds//3600) + " hour(s), "+ str(int((Uptime.seconds//60)%60)) + " minute(s) and " + str(int(Uptime.seconds%60)) + " second(s) </center>" + Al.read())', b'\tAf.close()', b'\tAl.close()', b'\tAw.close()', b'\tN.close()', b"\treturn render_template('about.html') #Displays HTML page 'Relay.html'", b'', b"@app.route('/source') #Sets index", b'def source():', b"\treturn send_file('Weather.py')", b'', b"if __name__ == '__main__':", b'\tapp.run(debug=True, host=(str(IP)), threaded=True, port=80)', b'GPIO.cleanup()']