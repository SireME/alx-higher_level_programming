#!/bin/bash
# dispaly HTTP methods server will accept
curl -sL $1 | grep Allow | cut -d " " -f 2-
