#!/bin/bash

ip=$(ifconfig ens33 | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1)

./print.py $ip
