#!/bin/bash
# send json post request
curl -sH "Content-Type: appliation/json" -d "$(cat "$2")" $1
