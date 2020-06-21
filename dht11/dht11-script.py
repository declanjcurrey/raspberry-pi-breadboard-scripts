import RPi.GPIO as GPIO
import dht11
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# connect to dht11 data pin on GPIO 4
instance = dht11.DHT11(pin = 4)

def log_error(error_code):
    print("Error Logged!")
    with open("./logs/dht11-error-logs.txt", "a") as log_file:
        log_file.write(" Error Logged! With error code {} at {} \n ".format(error_code, time.ctime()))

try: 
    while True:

        # read from the dht11 sensor
        result = instance.read()

        # if the reading from the dht11 is valid, print temperature
        if result.is_valid():
            print("****************************************************")
            print("Time reading recorded: " + time.ctime())
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            print("**************************************************** \n")
           
            # sleep the script for 2.5 seconds
            time.sleep(2.5)
        else:
            log_error(result.error_code)
except KeyboardInterrupt:
    print("Script interrupted via keyboard input... Cleaing up GPIO.")
    GPIO.cleanup()
    print("Script exited successfully.")
    

        
