import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2' 
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784], name='x') # 因为是None，既每次训练的数量不固定，batch取多少都可以
                               # None 的这个位置也只batch size

W = tf.Variable(tf.zeros([784,10]), name='W')
b = tf.Variable(tf.zeros([10]), name='b')
# b = tf.Variable(tf.zeros([1,10]), name='b') # b 这样写也可以
y = tf.nn.softmax(tf.matmul(x,W) + b) 

y_ = tf.placeholder("float", [None,10], name='y_') # 真实值,在训练的时候要代入真实值的，所以用占位符

#cross_entropy = -tf.reduce_sum(y_*tf.log(y))  # y_  哑变量
cross_entropy = tf.reduce_sum(tf.square(y_-y))  # 成本函数 这样也可以用， 0.92左右
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()
# 训练模型
with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        feed_dict = {x: batch_xs, y_: batch_ys}
        _, cost = sess.run([train_step, cross_entropy], feed_dict=feed_dict)
        #print('epoch {}: {}'.format(i, cost))
    #writer = tf.summary.FileWriter('./graphs', sess.graph) # cmd中键入tensorboard --logdir="./graphs" --port=6006 

    # 验证正确率 
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float")) # 在这里 softmax比 sigmoid 和 relu都高
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
    
    # 预测几个值
    # 预测就是run一下y  
    x1, y1 = mnist.train.next_batch(10)
    one_pred = sess.run(y, feed_dict={x:x1})
    print(y1, one_pred)
