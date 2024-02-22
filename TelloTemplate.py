# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nChristopher Melbow/Ryan Jerzyk/Madelyn Hershberger")
print("Program Name: Autonomous")
print("Date: 2.6.2024")
print("Drone WIFI = 4E1D")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')



if ready.lower() == 'yes':
    # first checkpoint
    print("\nStarting Drone!\n")
    sendmsg('battery?', 3)
    sendmsg('command')
    sendmsg('takeoff', 7)
    sendmsg('forward 210', 7)
    # Second Checkpoint
    sendmsg('go 225 0 40 50', 10)
    # Third Checkpoint
    sendmsg('curve 125 125 0 0 250 0 50', 12)
    sendmsg('cw 180', 7)
    sendmsg('forward 40', 7)

        # Review the (SDK) Software Development Kit resource for Drone Commands
        # Delete these comments before writing your program

    sendmsg('land')

    print('\nGreat Flight!!!')

else:
    print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')


breakr = True
sock.close()
