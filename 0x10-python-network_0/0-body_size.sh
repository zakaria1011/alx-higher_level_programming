#!/bin/bash
# isplays the size of the body of the http response
curl -s "$1" | wc -c
