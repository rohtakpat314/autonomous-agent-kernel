
from runtime.agent import Agent 
class Scheduler: 
    def run(self, agent: Agent):
        #Main loop that conducts the agent steps and handles the lifecycle/safety rails.
        running = True
        #for the loop
        while running:
            try:
                #not really sure how we would get the current state of the agent 
                #we know that these finite state machines work as 'stepping' from one state to another, so i put it as a step function
                status = agent.step()
                

                # Check for exit signals (STOP) or internal completion flags.
                if status.get("state") == "STOP" or status.get("done"):
                    #if the task is done then we can stop the loop
                    running = False
                
            except Exception as error:
                #Catching at the scheduler level prevents state corruption and allows for a clean exit/save
                #trigger a save here.
                is_running = False
