#!/bin/bash
# coding=utf-8

parallel \
    ./example.py --set-gamma {1} --set-c {2} \
    ::: 0.1 1 10 \
    ::: 0.2 2 20
