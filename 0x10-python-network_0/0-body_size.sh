#!/bin/bash
#sends a request to url, display the size of the body of the response
curl -sI &1 |grep -i Content-length | Awk '{print $2}'
