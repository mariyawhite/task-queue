# Task Queue

## Overview

A file-backed FIFO task queue with a worker that processes tasks safely using idempotent execution.

Designed to explore reliability, persistence, and task coordination, including handling duplicate processing and maintaining consistent state across runs.

## Features

- FIFO task ordering
- Idempotent task processing (prevents duplicate execution)
- Persistent storage using local text files
- CLI interface for interacting with the system
- Separation of concerns:
  - `queue.py` → CLI + queue management
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

## Next Steps
- support multiple workers
- add task identifiers (IDs)
- add timestamps for tasks
