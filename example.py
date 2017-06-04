#!/usr/bin/env python3
# coding=utf-8

import argparse
import pickle
from sklearn import (
    datasets,
    svm,
    metrics
)

parser = argparse.ArgumentParser(description="CLI utility with scikit-learn example training and testing on the Iris dataset.")
parser.add_argument('--set-gamma', metavar='gamma', dest='gamma', default=0.001, type=float, help='Gamma parameter for the SVM classifier.')
parser.add_argument('--set-c', metavar='C', dest='C', default=100., type=float, help='C parameter for the SVM classifier.')
args = parser.parse_args()

iris = datasets.load_iris()

clf = svm.SVC(gamma=args.gamma, C=args.C)
clf.fit(iris.data[:-10], iris.target[:-10])
with open(f'iris_svm_g{args.gamma}_c{args.C}.mdl', 'wb') as f:
    pickle.dump(clf, f)

y_pred = clf.predict(iris.data[-10:])
print('Accuracy:', metrics.accuracy_score(iris.target[-10:], y_pred), f'for gamma={args.gamma}, C={args.C}')

