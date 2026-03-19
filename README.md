# Task Queue

## Goal
A simple task queue system where:
- tasks are added to a queue
- a worker processes tasks one at a time
- each task is processed exactly once
- order is preserved (FIFO)

## Usage
Add tasks:
- resize_image_1
- resize_image_2

Worker output:
processing resize_image_1
processing resize_image_2

## Next Steps
- persist queue to disk (so tasks survive restart)
- prevent duplicate processing
- support multiple workers
