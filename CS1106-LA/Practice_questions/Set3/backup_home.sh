#!/bin/bash
backup_dir="/backups/home_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$backup_dir"
cp -r /home "$backup_dir/"
tar -czf "$backup_dir.tar.gz" "$backup_dir"
tar -tzf "$backup_dir.tar.gz" > /dev/null && echo "Backup successful" || echo "Backup failed"
