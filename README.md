# Optrace - Agent AI Runtime  

# Week 1 Progress

This project aims to build a lightweight, compact AI Agent Runtime for proof of concept. The goal is to make it similar to an operating system, but for AI agents.
The runtime schedules agents, manages their state, handles specific tool features, and provides an interface for handling AI tools. 

However, what does this actually prove? 

It proves that employers and big-tech companies could implement an internal layer specialized for AI. This would lead to less resource consumption and help with 
communication between AI's. Essentially, results from one AI could feed into another (I/O) in an n8n daisychain format. Additionally, it would allow for audittable 
actions and replay functionality to ensure that the AI agents are running responsibly and that their actions are being logged. 

Week 1 focused on laying the foundation: defining the core classes, making a simple tools interface, implementing counters, and establishing a robust architecture 
with elegant yet useful variable names for future development. 

# Week 1 Goals: 

1. Define **Agent**, **Scheduler**, **State**, and **Tool** Interfaces. Our backbone was inspired by introductory Linear Algebra and Engineering courses that work
with Markov Chains and Finite State Machines (FSMs). 
2. Implement a basic Agent and Scheduler loop.
3. Wire the scheduler to agents and actions. 
4. Add persistent state storage and an auditting system in C. 
5. Implement example tools provided by AI models, such as a calculator or file writer. 
6. Handle any failures to ensure state consistency and compliance. 
7. Review core concepts since we're students, such as Linear Algebra, I/O, Python Libraries, and FSMs. 

-- 

## Folder Structure 

    ai-agent-runtime/
    ├── agents/
    │ ├── init.py
    │ ├── base.py # Agent interface
    │ └── counter_agent.py # Example CounterAgent for testing
    ├── scheduler/
    │ ├── init.py
    │ └── scheduler.py # Scheduler loop implementation
    ├── tools/
    │ ├── init.py
    │ ├── base.py # Tool interface
    │ ├── calculator.py # Example calculator tool
    │ └── file_writer.py # Example file writing tool
    ├── storage/
    │ ├── init.py
    │ └── persistent_state.py # Persistent state and event logging
    ├── tests/
    │ └── test_counter_agent.py
    ├── README.md
    └── requirements.txt


*Founded by: Rohtak Patwardhan*
*Developed by Rohtak Patwardhan, Vikramaditya Rajput, and Akshit Jalli*   