'''
模仿mnist hello world
二进制转成十进制数字
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' 


x = tf.placeholder(tf.float32, shape=(None, 4) )
W = tf.Variable( tf.zeros([4, 10]) )  # [10, 4]其实就是shape
b = tf.Variable( tf.zeros([10]) )

# 激励函数可用 sigmoid softmax 
#y = tf.matmul(x, W) + b  # 是不是没有用激励函数
y = tf.nn.softmax(tf.matmul(x,W) + b)  # 
y_ = tf.placeholder(tf.float32, shape=[None, 10])

#cost = tf.reduce_mean( tf.pow((y_-y), 2) )  
cost = -tf.reduce_sum(y_*tf.log(y)) 
train_step = tf.train.GradientDescentOptimizer(1).minimize(cost)

init = tf.global_variables_initializer()

# 造数据集
xs = np.array([
    [0,0,0,0],  # 0
    [0,0,0,1],  # 1
    [0,0,1,0],  # 2
    [0,0,1,1],  # 3
    [0,1,0,0],  # 4
    [0,1,0,1],  # 5
    [0,1,1,0],  # 6
    [0,1,1,1],  # 7
    [1,0,0,0],  # 8
    [1,0,0,1],  # 9
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

    for i in range(999):
        idx = np.random.randint(10)  # 随机获取一个index
        feed_dict = {x: [xs[idx, :]],
                     y_: [ys[idx, :]]}
        sess.run( train_step, feed_dict=feed_dict )
    W_, b_ = sess.run([W,b])
    

# 预测n个值
with tf.Session() as sess:
    a = np.arange(10)
    np.random.shuffle(a)
    for n in a:
        y = tf.nn.softmax(tf.matmul(x, W_) + b_)
        feed_dict = {x: [xs[n, :]]}
        y_pred = sess.run(y, feed_dict=feed_dict)
        print('n {}: '.format(n), y_pred.argmax())
        #print(type(y_pred), y_pred.shape, y_pred.argmax())
    # 这个检验方式是针对输出结果是哑变量的
    #correct_prediction = tf.equal(tf.argmax(y_pred,1), tf.argmax(y,1))
    #accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    #print(sess.run(accuracy, feed_dict=feed_dict))