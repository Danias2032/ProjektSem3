from socket import *
import json
from time import sleep
import random
from datetime import datetime, time

serverName = 'Localhost'
serverPort = 11101
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sensorName = "Parking_space_sensor"

currentCars = 0
amountOfCars = 0
maxAmountOfCars = 150

while True:
    currentTime = datetime.now().time()
    if currentTime.hour < 12:
        amountOfCars += 2
    else:
        amountOfCars += 1
    currentCars = amountOfCars
    if amountOfCars > 50 and amountOfCars % 5 == 0:
        currentCars -= 1
    if currentCars > maxAmountOfCars:
        currentCars = maxAmountOfCars
    if currentCars > 124:
        sleep(random.randint(1,5))
    if currentCars > 145:
        sleep(random.randint(300,600))
    else:
        sleep(random.randint(0,0))
    carObject = {"Sensor": sensorName, "New car": currentCars, "Max cars": maxAmountOfCars}
    message = json.dumps(carObject)
    clientSocket.sendto(message.encode(), (serverName, serverPort))