#!/bin/bash

udisksctl status | grep -E "Mount Point" | awk '{print $2}'
