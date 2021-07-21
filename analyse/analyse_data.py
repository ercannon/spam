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