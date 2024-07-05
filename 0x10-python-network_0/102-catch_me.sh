#!/bin/bash
# Send request to 0.0.0.0:5000/catch_me to trigger specific response
curl -sX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
