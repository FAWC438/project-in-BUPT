# coding: utf-8

import tensorflow as tf
import numpy as np
import argparse
import os
import random
import time
import collections

batchSize = 64

learningRateBase = 0.001
learningRateDecayStep = 1000
learningRateDecayRate = 0.95

epochNum = 30                    # train epoch default=10
generateNum = 5                   # number of generated poems per time

type = "poetrySong"                   # dataset to use, poetrySong, shijing, songci, wangfeng, spider_shi etc
trainPoems = "./dataset/" + type + "/" + type + ".txt" # training file location
checkpointsPath = "./checkpoints/" + type # checkpoints location

saveStep = 1000                   # save model every savestep default=1000



# evaluate
trainRatio = 0.8                    # train percentage
evaluateCheckpointsPath = "./checkpoints/evaluate"