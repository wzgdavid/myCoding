'''
十进制数字转成二进制
加一个隐藏层
其实这个例子不好，因为一般输出都是one-hot的，但二进制不是
所以应该二进制转十进制
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


x = tf.placeholder(tf.float32, shape=(None, 4) )  # 输入层
W = tf.Variable( tf.zeros([4, 10]) )
b = tf.Variable( tf.zeros([10]) )

#y = tf.matmul(x, W) + b
y = tf.nn.softmax(tf.matmul(x,W) + b)   # 输出层
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

    for i in range(500):
        idx = np.random.randint(10)  # 随机获取一个index
        feed_dict = {x: [xs[idx, :]],
                     y_: [ys[idx, :]]}
        sess.run( train_step, feed_dict=feed_dict )
    W_, b_ = sess.run([W,b])

    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(sess.run(accuracy, feed_dict=feed_dict))

    # 所以这样预测，直接run 那个 y
    # 因为这个W b 在同一个session中，所以写在这里
    for i in range(3):
        feed_dict = {x: [xs[i, :]]}
        y_pred = sess.run(y, feed_dict=feed_dict)
        print('y_pred: ', y_pred, i)


# 预测一个值  
# 一开始想到的是得出训练完的W b 值 W_ b_
# 但这样没必要，其实训练好之后默认的W b 已经在y那个式子中，用不着特意得到
# 而且这个W是个很大的矩阵，打印出来也看不懂什么，除了这种很简单的例子
#with tf.Session() as sess:
#    y = tf.nn.softmax(tf.matmul(x, W_) + b_)
#    feed_dict = {x: [xs[0, :]]}
#    y_pred = sess.run(y, feed_dict=feed_dict)
#    print('y_pred: ', y_pred)

