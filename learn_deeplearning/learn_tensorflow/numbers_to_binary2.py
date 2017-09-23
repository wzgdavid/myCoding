'''
十进制数字转成二进制
加一个隐藏层
9月23  现在或许还实现不了，再学习学习继续这个
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#隐藏层1， nn个神经元
nn = 5
x = tf.placeholder(tf.float32, shape=(None, 10) )  # 输入层
W = tf.Variable( tf.zeros([10, nn]) )
b = tf.Variable( tf.zeros([nn]) )

x1 = tf.nn.softmax(tf.matmul(x,W) + b)
W1 = tf.Variable( tf.zeros([nn, 4]) )
b1 = tf.Variable( tf.zeros([4]) )

#y = tf.matmul(x, W) + b
y = tf.nn.softmax(tf.matmul(x1,W1) + b1)   # 输出层
y_ = tf.placeholder(tf.float32, shape=[None, 4])

#cost = tf.reduce_mean( tf.pow((y_-y), 2) )  
cost = -tf.reduce_sum(y_*tf.log(y)) 
train_step = tf.train.GradientDescentOptimizer(1).minimize(cost)

init = tf.global_variables_initializer()

# 造数据集
xs=np.array([
    [1,0,0,0,0,0,0,0,0,0],  # 0
    [0,1,0,0,0,0,0,0,0,0],  # 1
    [0,0,1,0,0,0,0,0,0,0],  # 2
    [0,0,0,1,0,0,0,0,0,0],  # 3
    [0,0,0,0,1,0,0,0,0,0],  # 4
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,1],  # 9
    ])
ys = np.array([
    [0,0,0,0],  # 0
    [0,0,0,1],  # 1
    [0,0,1,0],
    [0,0,1,1],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],   # 9
    ])

with tf.Session() as sess:
    sess.run(init)

    for i in range(9999):
        idx = np.random.randint(10)  # 随机获取一个index
        feed_dict = {x: [xs[idx, :]],
                     y_: [ys[idx, :]]}
        sess.run( train_step, feed_dict=feed_dict )
    W_, b_ = sess.run([W,b])

    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(sess.run(accuracy, feed_dict=feed_dict))


# 预测一个值
with tf.Session() as sess:
    y = tf.nn.softmax(tf.matmul(x, W_) + b_)
    feed_dict = {x: [xs[1, :]]}
    y_pred = sess.run(y, feed_dict=feed_dict)
    print('y_pred: ', y_pred)