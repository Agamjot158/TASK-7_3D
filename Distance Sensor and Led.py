import time                             
from time import sleep                  #importing time library and its sleep function
import RPi.GPIO as GPIO                  
from gpiozero import Reading
from gpiozero import PWMLED

GPIO.setmode(GPIO.BOARD)                  #using GPIO naming convention

LED = PWMLED(18)       # setting up the led at GPIO 18
ECHO = 23              #setting ultrasonic sensor and definig its pins
TRIGGER = 24                  
Distance = Reading(echo=23, trigger=24)   

try: 
   
    while True:                           
       distance = Distance.reading * 100    #converting distance into cm from metre
       print('Distance = ', distance)      #printing the value to terminal
   
        if(distance < 20):                  #if case for values lower than 20.
            LED.value = 1 - (distance / 20)  #setting the value of the pwm buzzer to 1 - (distance / 20). eg. - let distance be 15. in that case, pwm value will be 1 - 3/4 = 1/4.
        
        else:     # if the value is greater that 20
          
         LED.off
  
    except KeyboardInterrupt:
    GPIO.cleanup() 
