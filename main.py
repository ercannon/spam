#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:42:56 2021

@author: cannon
"""

from fetcher.fetch_data import fetch_data
from datamanagement.analyse_data import load_mails
from datamanagement.analyse_data import structures_counter

#fetch_data()
ham_emails,spam_emails=load_mails()
print(structures_counter(ham_emails).most_common())
