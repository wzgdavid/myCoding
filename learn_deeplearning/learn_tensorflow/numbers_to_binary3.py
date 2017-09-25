'''
在2的基础上加一个隐藏层
9月25日
还是不会改，不会预测
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


n = 5 # 隐藏层5个神经元
x = tf.placeholder(tf.float32, shape=(None, 4) )  # 输入层
W = tf.Variable( tf.zeros([4, n]) )
b = tf.Variable( tf.zeros([n]) )


x1 = tf.nn.softmax(tf.matmul(x,W) + b)
W1 = tf.Variable( tf.zeros([n, 10]) )
b1 = tf.Variable( tf.zeros([10]) )
 

y = tf.nn.softmax(tf.matmul(x1,W1) + b1)   # 输出层
y_ = tf.placeholder(tf.float32, shape=[None, 10])

#cost = tf.reduce_mean( tf.pow((y_-y), 2) )  
cost = -tf.reduce_sum(y_*tf.log(y)) 
train_step = tf.train.GradientDescentOptimizer(1).minimize(cost)

init = tf.global_variables_initializer()

# 造数据集
xs = np.array([
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
ys=np.array([
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

with tf.Session() as sess:
    sess.run(init)

    for i in range(200):
        idx = np.random.randint(10)  # 随机获取一个index
        feed_dict = {x: [xs[idx, :]],
                     y_: [ys[idx, :]]}
        sess.run( train_step, feed_dict=feed_dict )
    W_, b_ = sess.run([W1,b1])
    #print(W_, b_)
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(sess.run(accuracy, feed_dict=feed_dict))


# 预测一个值
#with tf.Session() as sess:
#    y = tf.nn.softmax(tf.matmul(x, W_) + b_)
#    feed_dict = {x: [xs[3, :]]}
#    y_pred = sess.run(y, feed_dict=feed_dict)
#    print('y_pred: ', y_pred)