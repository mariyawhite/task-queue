# Task Queue

## Overview

A file-backed FIFO task queue with a worker that processes tasks and tracks completed work to avoid duplicate execution.

Built to explore persistence, idempotency, and the interaction between a queue and a worker process.

## Features

- FIFO task ordering
- Persistent storage using local text files
- Structured tasks stored as JSON (type, id, task data)
- Idempotent processing using unique task IDs
- CLI interface for adding and processing tasks
- Separation of concerns:
  - `queue.py` → queue management and CLI
  - `worker.py` → task processing

## Usage

### Add tasks
```bash
python3 queue.py add task1
python3 queue.py add task2
```

### Process tasks
```bash
python3 queue.py run
```

### Output
```bash
processing task1
processing task2
```
