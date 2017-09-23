'''
十进制数字转成二进制
'''
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' 


x = tf.placeholder(tf.float32, shape=(None, 10) )
W = tf.Variable( tf.zeros([10, 4]) )
b = tf.Variable( tf.zeros([4]) )

#y = tf.matmul(x, W) + b
y = tf.nn.softmax(tf.matmul(x,W) + b)
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

    for i in range(99999):
        idx = np.random.randint(10)  # 随机获取一个index
        feed_dict = {x: [xs[idx, :]],
                     y_: [ys[idx, :]]}
        sess.run( train_step, feed_dict=feed_dict )
    print(sess.run([W,b]))

    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(sess.run(accuracy, feed_dict=feed_dict))

#[array([[ 0.        ,  0.        ,  0.        ,  0.        ],
#       [-1.35087454, -2.70348215, -2.68072891,  6.73475647],
#       [-1.40772378, -2.76683831,  7.73852444, -3.56427217],
#       [-3.17997289, -5.13133526,  4.70337105,  3.60793853],
#       [-1.37526608,  7.74654293, -2.8053236 , -3.56620646],
#       [-3.22232914,  4.7174654 , -5.12197399,  3.62679076],
#       [-3.26112342,  4.67811251,  4.68281555, -6.09981918],
#       [-5.23044682,  2.10876775,  2.10989833,  1.01179576],
#       [ 9.89613056, -3.04181051, -3.02874827, -3.82572794],
#       [ 7.02894497, -5.2636528 , -5.26226282,  3.49695659]], dtype=float32), array([-2.10260057,  0.34405318,  0.33590332,  1.42266285], dtype=float32)]
#1.0