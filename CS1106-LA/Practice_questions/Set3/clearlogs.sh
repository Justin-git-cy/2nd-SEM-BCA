#!/bin/bash
log_archive="/var/log/logs_$(date +%Y%m%d).tar.gz"
ls /var/log/*.log
tar -czf "$log_archive" /var/log/*.log
truncate -s 0 /var/log/*.log
echo "Logs archived to $log_archive and cleared."
