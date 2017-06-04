#!/bin/bash
# coding=utf-8

# Caution: if localhost is also a node, you may need to manually copy the "--basefile" argument to the "--workdir".

parallel --sshloginfile nodefile --workdir ~/parallel-example --basefile example.py --return "iris_svm_g{1}_c{2}.mdl" \
    ./example.py --set-gamma {1} --set-c {2} \
    ::: 0.1 1 10 \
    ::: 0.2 2 20
