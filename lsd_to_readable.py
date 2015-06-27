import pandas as pd


import os

import sys


time_df = pd.read_csv(sys.argv[1])
pose_df = pd.read_csv(sys.argv[2])

#print(time_df.dtypes)
#print(pose_df.dtypes)
orig_time = time_df.field #you can also use df['column_name']

print(pose_df.dtypes)

q_x = pose_df.field0
q_y = pose_df.field1
q_z = pose_df.field2
q_w = pose_df.field3
pos_x = pose_df.field4
pos_y = pose_df.field5
pos_z = pose_df.field6

formatted_out = pd.concat((orig_time,pos_x,pos_y,pos_z,q_x,q_y,q_z,q_w),1)
#print(formatted_out)


formatted_out.to_csv(sys.argv[3],index = False, header = False)
