#!/bin/bash
#sends a request to url, display the size of the body of the response
curl -sI &1 | grep -i content-length | awk '{print $2}'
