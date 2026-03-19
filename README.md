# Task Queue

## Goal
A simple task queue system where:
- tasks are added to a queue
- a worker processes tasks one at a time
- each task is processed exactly once
- order is preserved (FIFO)

## Example
Add tasks:
- resize_image_1
- resize_image_2

Worker output:
processing resize_image_1
processing resize_image_2
