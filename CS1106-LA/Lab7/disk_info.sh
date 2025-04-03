#!/bin/bash

# Use udisksctl to list mounted filesystems
udisksctl status | grep -E "Mount Point" | awk '{print $2}'

# Alternatively, use udisksctl info to get more details
# udisksctl info --block-device /dev/sdXN | grep "Mount Point"
