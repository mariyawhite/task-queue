# Task Queue

## Goal
A simple task queue system where:
- tasks are added to a queue
- a worker processes tasks one at a time
- each task is processed exactly once
- order is preserved (FIFO)

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
