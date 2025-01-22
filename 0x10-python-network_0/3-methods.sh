#!/bin/bash
# takes an URL,displays all HTTP methods accepted by the server
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
