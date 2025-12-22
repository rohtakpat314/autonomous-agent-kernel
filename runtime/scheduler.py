# Created by Rohtak Patwardhan. 2025. 

from runtime.agent import Agent 

"""

Controls execution of agent. The Scheduler owns time, step count, tool exec., failure handling
and persistence and replay. 

"""

class Scheduler: 

    def run(self,agent: Agent):
        raise NotImplementedError

""" 

Execute the agent until STOP or failure. 

Guarantees that at most one Agent.step() call, all actions are validated, and all state
transitions are observable / audittable. 

"""