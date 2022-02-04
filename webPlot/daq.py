import multiprocessing
import time

from webPlot import socketio
from webPlot.sensor.RandomDataSensor import RandomDataSensor


def startDAQ(queue: multiprocessing.Queue):
    # Do something
    interval = 0.1

    # Init sensor
    random_sensor = RandomDataSensor()

    # Init time
    current_time = 0
    last_time = time.time()

    while True:
        # Read out the sensor, if
        current_time = time.time()
        if current_time - last_time > interval:
            data = random_sensor.get_data()
            queue.put({"data": data, "time": current_time})

            # Update the latest time
            last_time = current_time
