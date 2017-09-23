'''
多元线性回归
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告

feature_num = 2 # 特征数量
x = tf.placeholder( tf.float32, shape=[None, feature_num] )
W = tf.Variable( tf.zeros([feature_num, 1]) )
b = tf.Variable( tf.zeros([1]) )
y = tf.matmul(x, W) + b

y_ = tf.placeholder(tf.float32, shape=[None, 1])

# 成本函数
cost = tf.reduce_mean( tf.pow((y_-y), 2) )   

train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(cost)


# 训练模型
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    
    for i in range(90):
        # 假数据
        xs = np.array([[i,i]])
        # 简单起见，我们将房价 (ys) 设置成永远是房子面积 (xs) 的 2 倍。
        ys = np.array([[3*i + 2*i]]) 

        feed = {x:xs, y_:ys}
        sess.run(train_step, feed_dict=feed)
        print(sess.run([W,b]))