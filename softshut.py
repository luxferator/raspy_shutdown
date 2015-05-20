# Import the modules to send commands to the system and access GPIO pins

# Pi Supply Soft Shutdown Script


2.# Version 1.1


3.# Nathan Bookham 2013


4. 


5.# Import the modules to send commands to the system and access GPIO pins


from subprocess import call


import RPi.GPIO as gpio


 


# Define a variable to store the pin number


soft_shutdown_pin = 7 # Default pin for Pi Supply is 7


 


# Define a function to run when an interrupt is called

def shutdown():


    call('halt', shell=False)


 


gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering


gpio.setup(soft_shutdown_pin, gpio.IN) # Set up pin 7 as an input


 

gpio.wait_for_edge(soft_shutdown_pin, gpio.RISING) # Wait for input from button


 


shutdown() # Run the shutdown function

