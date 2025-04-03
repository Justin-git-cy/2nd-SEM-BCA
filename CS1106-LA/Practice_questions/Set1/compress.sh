#!/bin/bash
tar -cvf logs.tar /var/log
gzip logs.tar
ls -lh logs.tar.gz
