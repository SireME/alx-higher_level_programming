#!/bin/bash
# send get request and display response body send along headerwith value as seen
curl -sH "X-School-User-Id: 98" "$1"
