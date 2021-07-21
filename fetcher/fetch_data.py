#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:43:11 2021

@author: cannon
"""
import os
import tarfile
import urllib.request
import constants.constants as const


def fetch_data(ham_url=const.HAM_URL, spam_url=const.SPAM_URL, spam_path=const.SPAM_PATH):
    if not os.path.isdir(spam_path):
        os.makedirs(spam_path)
    
    for filename,url in (("ham.tar.bz2",ham_url),("spam.tar.bz2",spam_url)):
        path = os.path.join(spam_path, filename)
        if not os.path.isfile(path):
            urllib.request.urlretrieve(url,path)
        tar_bz2_file=tarfile.open(path)
        tar_bz2_file.extractall(path=spam_path)
        tar_bz2_file.close()
    