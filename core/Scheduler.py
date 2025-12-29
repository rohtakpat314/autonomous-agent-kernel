from core.agent import Agent
from core.state import State
from core.action import Action

class Scheduler:
    def __init__(self, max_steps: int = 100):
        self.max_steps = max_steps

    def run(self, agent: Agent, state: State):
        running = True
        steps = 0

        while running and steps < self.max_steps:
            try:
                action: Action = agent.step(state)
                self.apply_action(state, action)

                if action.type == "STOP":
                    running = False

                steps += 1
                state.step_count += 1

            except Exception as error:
                print(f"Error in agent step: {error}")
                running = False

    def apply_action(self, state: State, action: Action):
        if action.type == "SET":
            key, value = action.payload
            state.set(key, value)
        elif action.type in ("NOOP", "STOP"):
            pass
        else:
            raise ValueError(f"Unknown action type: {action.type}")
