# 
#
#
# usage: python ate_test.py slam_dataset groundtruth dataset
#
#
#


import matlab.engine
#from subprocess import call
import os

import sys

print "\n".join(sys.argv)

eng = matlab.engine.start_matlab()

# CHANGE THE PATH HERE TO LINK TO PYTHON SCRIPT
eng.addpath(r'/home/bomp/pythonscripts',nargout=0)


#cmd = 'python associate.py > associated_timestamps.txt dataset/freib_scale_same_scale_test.txt dataset/groundtruth_matlab.txt'

cmd = 'python associate.py > associated_timestamps.txt ' + sys.argv[1] + ' ' + sys.argv[2]
os.system(cmd)


s = eng.getScale()


print(s,"  ", type(s), "\n")


#cmd = 'python evaluate_ate.py --plot figure.png --offset 0 --scale ' + str(s) + ' --verbose dataset/groundtruth_matlab.txt dataset/freib_scale_same_scale_test.txt'

cmd = 'python evaluate_ate.py --plot figure.png --offset 0 --scale ' + str(s) + ' --verbose ' + sys.argv[2] + ' ' + sys.argv[1]


os.system(cmd)

