# Task Queue

## Overview

A file-backed FIFO task queue with a worker that processes tasks exactly once.

Designed to explore reliability, persistence, and task coordination, including handling duplicate processing and maintaining consistent state across runs.

## Features

- FIFO task ordering  
- Exactly-once processing (idempotent execution)  
- Persistent storage using text files  
- Separation of concerns:
  - `tasks.py` → add tasks  
  - `queue.py` → manage queue  
  - `worker.py` → process tasks  

## Usage

### Add tasks
```bash
python3 tasks.py
```

### Run worker
```bash
python3 worker.py
```

### Output
```bash
processing task1
processing task2
```

## Next Steps
- support multiple workers
- build a CLI interface for adding and processing tasks
