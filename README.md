# Supermarket_Management_DB

## Overview
This project implements a database-driven simulation system for managing a supermarket chain. It handles employees, suppliers, branches, products, and dynamic activity logs such as sales and deliveries, all using a command-line interface and a SQLite database.

## Features
- Initialize a complete supermarket database from configuration files.
- Execute business actions such as sales and restocking via input files.
- Persistent SQLite storage with multiple interconnected tables.
- Utility scripts to print the current state of the database.

## Build and Run

### Requirements
- Python 3.7+
- `sqlite3` (pre-installed in most environments)

### Run Initialization
```bash
python3 initiate.py config.txt
```

### Run Actions
```bash
python3 action.py action.txt
```

### View Database State
```bash
python3 printdb.py
```

All files (`config.txt`, `action.txt`, etc.) must be placed in the root directory for proper execution.