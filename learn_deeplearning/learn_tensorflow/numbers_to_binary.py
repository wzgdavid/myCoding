'''
十进制数字转成二进制
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' 


x = tf.placeholder(tf.float32, shape=(None, 10) )
W = tf.Variable( tf.ones([10, 4]) )
b = tf.Variable( tf.ones([4]) )

y = tf.matmul(x, W) + b
y_ = tf.placeholder(tf.float32, shape=[None, 4])

cost = tf.reduce_mean( tf.pow((y_-y), 2) )  
train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(cost)

init = tf.global_variables_initializer()
# 训练模型
with tf.Session() as sess:
    sess.run(init)
    feed_dict = {x:np.arange(10).reshape(1,-1)}
    print(sess.run( y, feed_dict=feed_dict))