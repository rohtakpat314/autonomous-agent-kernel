from core.state import State
from core.scheduler import Scheduler
from agents.counter_agent import CounterAgent

state = State()
agent = CounterAgent("counter1")
scheduler = Scheduler(max_steps=10)

scheduler.run(agent, state)

print(state)
