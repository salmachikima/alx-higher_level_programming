#!/bin/bash
# send delete request to the URL passed at the first argument
curl -sX DELETE "$1"
