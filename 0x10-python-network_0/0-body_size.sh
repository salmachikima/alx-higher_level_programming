#!/bin/bash
# Take URL, send request to it and display the size
curl -s "$1" | wc -c
