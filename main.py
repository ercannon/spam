#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:42:56 2021

@author: cannon
"""

from fetcher.fetch_data import fetch_data
from datamanagement.analyse_data import load_mails
from datamanagement.analyse_data import structures_counter
from datamanagement.data_split import split_data
from datamanagement.clean_data import preprocess_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score, recall_score


#fetch_data()
ham_emails,spam_emails=load_mails()
#print(structures_counter(ham_emails).most_common())
x_train, x_test, y_train, y_test = split_data(ham_emails, spam_emails)
x_train_transformed = preprocess_data(x_train)
log_clf = LogisticRegression(solver="lbfgs", max_iter=1000, random_state=42)
score = cross_val_score(log_clf, x_train_transformed, y_train, cv=3, verbose=3)
score.mean()

x_test_transformed = preprocess_data(x_test)
log_clf = LogisticRegression(solver="lbfgs", max_iter=1000, random_state=42)
log_clf.fit(x_train_transformed, y_train)

y_pred = log_clf.predict(x_test_transformed)

print("Precision: {:.2f}%".format(100 * precision_score(y_test, y_pred)))
print("Recall: {:.2f}%".format(100 * recall_score(y_test, y_pred)))


