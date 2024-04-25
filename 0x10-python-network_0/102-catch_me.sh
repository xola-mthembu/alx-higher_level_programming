#!/bin/bash
# This script tricks the server into responding with "You got me!"
curl -sLX PUT "0.0.0.0:5000/catch_me" -H "origin: HolbertonSchool" -d "user_id=98"
