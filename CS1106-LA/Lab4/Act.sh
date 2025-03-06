#!/bin/bash

mkdir shell-backup

cp *.sh shell-backup/

tar -cvf shell-backup.tar shell-backup/
