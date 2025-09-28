#!/bin/bash
curl -X POST http://localhost:8000/webhook \
  -H 'Content-Type: application/json' \
  -d '{"event": "user_created", "data": {"first_name": "John", "last_name": "Doe"}}'
