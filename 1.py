import random
import simpy

class RepairsSimulator:
    
    def __init__(self):            
        # You must set the values of these variables during the execution of the simulation:
        self.nr_repairs = 0 # The number of repairs that arrived
        self.nr_repairs_processed = 0 # The total number of repairs that was processed to completion
        self.sojourn_time_per_repair = 0 # The average sojourn time of repairs that were processed to completion
        self.service_time_per_repair = 0 # The average service time of repairs that were processed to completion
        self.waiting_time_per_repair = 0 # The average waiting time of repairs that were processed to completion                
        
    # seed: the random seed with which the simulator is initiated
    # duration: the amount of simulation time for which the simulator has to run
    def simulate(self, seed, duration):
        random.seed(seed) # use this line to set the seed
        
        env = simpy.Environment()

        # use the duration that was passed to the function, do not hardcode the duration
        
        # YOU CAN COMPLETE THIS FUNCTION BY ADDING YOUR OWN CODE HERE

        return env

##########################
##### SOLUTION CHECK #####
##########################

print("\n\nDISCLAIMER\nNote that if you pass the solution check that does not mean that you will get full points. "+
      "We will test more and different things. Also note that you should see DONE at the end of the tests. "+
      "If you do not see DONE, this means that the program got stuck somewhere and consequently does not work properly. "+
      "Finally, note that you must use all attributes and functions that are defined in the template and give them correct values according to the assignment description. "+
      "You must not change names or signatures of predefined classes, attributes or functions. Doing so may lead to severe deduction of points. "+
      "\n\nRESULTS")

print("\nSIMULATION 1:")
simulation_1 = RepairsSimulator()
env_1 = simulation_1.simulate(2019, 10000)
print("Duration: ", env_1.peek())
print("Nr repairs arrived: ", simulation_1.nr_repairs)
print("Nr repairs processed: ", simulation_1.nr_repairs_processed)
print("Sojourn time per repair: ", simulation_1.sojourn_time_per_repair)
print("Waiting time per repair: ", simulation_1.waiting_time_per_repair)
print("Service time per repair: ", simulation_1.service_time_per_repair)

#SIMULATION 2, TO CHECK IF NO INFORMATION IS KEPT FROM THE PREVIOUS SIMULATION RUN
print("\nSIMULATION 2:")
simulation_2 = RepairsSimulator()
env_2 = simulation_2.simulate(2020, 5000)
print("Duration: ", env_2.peek())
print("Nr repairs arrived: ", simulation_2.nr_repairs)
print("Nr repairs processed: ", simulation_2.nr_repairs_processed)
print("Sojourn time per repair: ", simulation_2.sojourn_time_per_repair)
print("Waiting time per repair: ", simulation_2.waiting_time_per_repair)
print("Service time per repair: ", simulation_2.service_time_per_repair)

print("\nDONE\n")

