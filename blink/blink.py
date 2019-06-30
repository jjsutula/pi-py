import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.out)
print("Python: Time to blink.")
for i in range(1, 10):
    GPIO.output(17, GPIO.HIGH)
    sleep(1)
    GPIO.output(17, GPIO.LOW)
    sleep(0.5)
GPIO.cleanup()

# Do this so that main() only gets called if invoked via command line, but not if invoked programmatically
if __name__ == "__main__":
    main(sys.argv[1:])
