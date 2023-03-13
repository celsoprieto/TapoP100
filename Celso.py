from PyP100 import PyP100

p100 = PyP100.P100("192.168.1.34", "celsoprieto@hotmail.com", "Celso3192") #Creates a P100 plug object

p100.handshake() #Creates the cookies required for further methods
p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods

cc= p100.turnOn() #Turns the connected plug on
p100.turnOff()