#!/bin/bash
# sends request to URL passed as an arg,display the status
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
