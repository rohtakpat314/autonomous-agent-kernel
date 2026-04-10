# Optrace - Agent AI Runtime 

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](#)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

This project aims to build a lightweight, compact AI Agent Runtime for proof of concept.  
The goal is to make it similar to an operating system, but for AI agents.  
The runtime schedules agents, manages their state, handles specific tool features, and provides an interface for handling AI tools.  


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
