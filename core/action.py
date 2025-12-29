# Created by Rohtak Patwardhan. 2025. 

"""
An Action is defined as a request from an Agent to the Scheduler. 

The Scheduler is the ONLY component allowed to: 
1. Advance time
2. Execute tools 
3. Stop execution

Agents must not cause side effects.

"""


from dataclasses import dataclass
from typing import Dict, Any  

@dataclass(frozen = True)   # frozen prevents mutation after a decision
class Action: 
    type: str               # "wait" 
    payload: Dict[str,Any] = None  
