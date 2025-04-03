#!/bin/bash

process_name="$1"

if [ -z "$process_name" ]; then
  echo "Usage: $0 <process_name>"
  exit 1
fi

pkill -9 "$process_name"

echo "'$process_name' terminated."
