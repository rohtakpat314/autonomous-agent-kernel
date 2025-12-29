# Created by Rohtak Patwardhan. 2025. 

from typing import Dict
from core.action import Action

"""

An Agent owns an ID, has a serializable state, and produces exactly one action per step. 

Agents are deterministic given (state, observation).

"""

class Agent: 
    def __init__(self,agent_id: str):
        self.agent_id = agent_id
        self.state: Dict = {}
    def step(self,state: Dict) -> Action: 
        raise NotImplementedError 
    
    """ 

    Perform exactly one decision step.

    Must not perform side effects, must not sleep or block, must return an action,
    and must only mutate the provided state.

    """