import time 

# Function to simulate the movements of Achilles and the tortoise in a way that appear that achilles never will reach tortoise

def zeno_paradox(): 
    achilles_position = 0 
    tortoise_position = 50 
    achilles_velocity = 10
    tortoise_velocity = 1 
    timeframe = 1 # Time frame will be lower each loop iteraction in order to generate the paradox perception
    Turn = 0

    # While tortoise_position greater than achilles keep looping
    while tortoise_position > achilles_position: 

        # Update speed, position and timeframe (to give Zeno's perception)
        achilles_position += achilles_velocity 
        tortoise_position += tortoise_velocity
        achilles_velocity = achilles_velocity//timeframe 
        tortoise_velocity = tortoise_velocity//timeframe 
        timeframe = timeframe+0.0626
        Turn +=1
        # Print the positions graphically and give a delay to give an animation perception
        print("\n\nRound: ", Turn)
        print("\n \r Achilles: [{}]".format("#" * int(achilles_position)))
        print("\n \r Tortoise: [{}]".format("-" * int(tortoise_position)))
        time.sleep(0.4) 

# Call the function to run the simulation 
zeno_paradox() 