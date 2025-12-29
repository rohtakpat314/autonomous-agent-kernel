from core.agent import Agent
from core.state import State
from core.action import Action

class CounterAgent(Agent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id)

    def step(self, state: State) -> Action:
        state.increment("count")

        if state.get("count") > 5:
            return Action(type="STOP")

        return Action(type="SET", payload=("count", state.get("count")))
