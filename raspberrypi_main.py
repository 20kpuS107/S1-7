import socket
import serial
import posix
from fcntl import ioctl
import RPi.GPIO as GPIO
import time
import os
import threading
from random import *

serial_data = ''

arduino=serial.Serial("/dev/ttyACM0",115200)

def read_serial():
    global serial_data
    while True:
        read_ser=arduino.readline()
        serial_data =read_ser.decode()[:-2]

read_serial_thread = threading.Thread(target=read_serial)
read_serial_thread.start()

HOST = ""
PORT = 8888
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ('Socket created')
s.bind((HOST, PORT))
print ('Socket bind complete')
s.listen(1)
print ('Socket now listening')



def do_some_stuffs_with_input(input_string):
    global serial_data
    if input_string == "request": 
        input_string= serial_data
    
    return input_string
while True: 
    conn, addr = s.accept() #
    print("Connected by ", addr)
    data = conn.recv(1024)
    data = data.decode("utf8").strip()
    if not data: break 
    print("Received: " + data)
    res = do_some_stuffs_with_input(data)
    print("transmit: "+ res)
    conn.sendall(res.encode("utf-8"))
    conn.close()
s.close()
