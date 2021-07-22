#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 19:00:44 2021

@author: cannon
"""

import numpy as np
from sklearn.model_selection import train_test_split


def split_data(ham_emails, spam_emails):
    X = np.array(ham_emails + spam_emails, dtype=object)
    y = np.array([0] * len(ham_emails) + [1] * len(spam_emails))
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test