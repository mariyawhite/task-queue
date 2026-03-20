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
# example (from Python REPL or script)
add_task("resize_image_1")
add_task("resize_image_2")
```

### Run worker
```bash
python3 worker.py
```

### Output
```bash
processing resize_image_1
processing resize_image_2
```

## Next Steps
- persist queue to disk (so tasks survive restart)
- prevent duplicate processing
- support multiple workers
- move task creation into a script or CLI command
