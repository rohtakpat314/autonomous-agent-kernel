# Optrace - Agent AI Runtime 

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](#)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

---

## Week 1 Progress

This project aims to build a lightweight, compact AI Agent Runtime for proof of concept.  
The goal is to make it similar to an operating system, but for AI agents.  
The runtime schedules agents, manages their state, handles specific tool features, and provides an interface for handling AI tools.  

However, what does this actually prove?  

It proves that employers and big-tech companies could implement an internal layer specialized for AI.  
This would lead to less resource consumption and help with communication between AIs.  
Essentially, results from one AI could feed into another (I/O) in an [n8n](https://n8n.io/) daisychain format.  
Additionally, it would allow auditable actions and replay functionality to ensure that the AI agents are running responsibly and that their actions are being logged.  

Week 1 focused on laying the foundation: defining the core classes, making a simple tools interface, implementing counters, and establishing a robust architecture with elegant yet useful variable names for future development.  

---

## Week 1 Goals

1. Define [Agent](./agents/base.py), [Scheduler](./scheduler/scheduler.py), [State](./storage/persistent_state.py), and [Tool](./tools/base.py) Interfaces  
   Inspired by introductory Linear Algebra and Engineering courses that work with Markov Chains and Finite State Machines (FSMs).  
2. Implement a basic Agent and Scheduler loop  
3. Wire the scheduler to agents and actions  
4. Add persistent state storage and an auditing system in C  
5. Implement example tools provided by AI models, such as a [calculator](./tools/calculator.py) or [file writer](./tools/file_writer.py)  
6. Handle any failures to ensure state consistency and compliance  
7. Review core concepts, such as Linear Algebra, I/O, Python Libraries, and FSMs  

---

## Folder Structure

    ai-agent-runtime/
    ├── agents/
    │ ├── init.py
    │ ├── base.py 
    │ └── counter_agent.py 
    ├── scheduler/
    │ ├── init.py
    │ └── scheduler.py 
    ├── tools/
    │ ├── init.py
    │ ├── base.py # Tool interface
    │ ├── calculator.py 
    │ └── file_writer.py 
    ├── storage/
    │ ├── init.py
    │ └── persistent_state.py 
    ├── tests/
    │ └── test_counter_agent.py
    └── README.md

---

<<<<<<< HEAD
**Founded by:** [Rohtak Patwardhan](https://github.com/rohtakpat314)  
**Developed by:** Rohtak Patwardhan, Vikramaditya Rajput, and Akshit Jalli
=======
*Founded by: Rohtak Patwardhan*

*Developed by Rohtak Patwardhan, Vikramaditya Rajput, and Akshit Jalli*   
>>>>>>> f512010b1a580f229386bdf1718244c920897d07
