# coding = utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import re
import json
import tarfile
import ConfigParser

from six.moves import urllib

from tensorflow.python.platform import gfile
import tensorflow as tf
import numpy as np
import math, os, sys

reload(sys)
sys.setdefaultencoding('utf8')
config = ConfigParser.ConfigParser()
config.read('config')

data_dir = "/home/local/LABINFO/2106457/Documents/ecm"

train_path = os.path.join(data_dir, 'train_data.json')
train_file = json.load(open(train_path,'r'))

new_file = []; set_t = {}

for i in train_file:
    i[0].append(0); i[1].append(0)
    new_file.append([i[0], [i[1] ]])

#for i in range(len(train_file)):
#    for j in train_file[i][0][0].split(" "):
#            set_t[j] = train_file[i][0][1]
#    for j in train_file[i][1]:
#        for m in j[0].split(" "):
#            set_t[m] = j[1]

#train_path = os.path.join(data_dir, 'data/vocab5.ememory')
#train_file = json.load(open(train_path,'r'))

json.dump(new_file, open( 'train_t', 'w' ), ensure_ascii=False, indent=4)

