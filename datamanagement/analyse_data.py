#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:10:14 2021

@author: cannon
"""

import email
import email.policy
import os
import constants.constants as cons
import glob
from collections import Counter

def load_mail(is_spam,filename,spam_path=cons.SPAM_PATH):
    with open(filename,"rb") as f:
        return email.parser.BytesParser(policy=email.policy.default).parse(f)

def load_mails():
    ham_dir = os.path.join(cons.SPAM_PATH,"easy_ham")
    spam_dir = os.path.join(cons.SPAM_PATH,"spam")
    ham_filenames = glob.glob(ham_dir + "/*.*")
    spam_filenames = glob.glob(spam_dir + "/*.*")
    ham_emails =[load_mail(False,filename=name) for name in ham_filenames]
    spam_emails =[load_mail(True,filename=name) for name in spam_filenames]
    return ham_emails,spam_emails

#vamos a separar el texto de aduntos y demas
def get_email_structure(email):
    if isinstance(email,str):
        return email
    payload = email.get_payload()
    if isinstance(payload, list):
        return "multipart({})".format(", ".join([
            get_email_structure(sub_email)
            for sub_email in payload
        ]))
    else:
        return email.get_content_type()
    
def structures_counter(emails):
    structures = Counter()
    for _email in emails:
        structure = get_email_structure(_email)
        structures[structure] += 1
    return structures
            
            
            
            
            
            
            
            
            