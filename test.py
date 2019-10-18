# -*- coding:utf-8 -*-

import tensorflow as tf

a =tf.Variable([1,2])
print(a)

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
