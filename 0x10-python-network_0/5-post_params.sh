#!/bin/bash
# send POST request with 2 parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
