import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' 
import time

'''
一元线性回归，写过了
'''


def huber_loss(labels, predictions, delta=1.0):
    residual = tf.abs(predictions - labels)
    condition = tf.less(residual, delta)
    small_res = 0.5 * tf.square(residual)
    large_res = delta * residual - 0.5 * tf.square(delta)
    return tf.select(condition, small_res, large_res)

'''
mnist做数据
简单逻辑回归
'''
from tensorflow.examples.tutorials.mnist import input_data

learning_rate = 0.1
batch_size = 128
n_epochs = 500

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

X = tf.placeholder(tf.float32, [batch_size, 784], name='X_placeholder')
Y = tf.placeholder(tf.float32, [batch_size, 10], name='Y_placeholder')

w = tf.Variable(tf.random_normal(shape=(784,10), stddev=0.01), name='w')
b = tf.Variable(tf.zeros([1, 10]), name='bias')

# build model
logits = tf.matmul(X, w) + b

# loss function
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y, name='loss')
loss = tf.reduce_mean(entropy)

# define training op
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    start_time = time.time()
    sess.run(tf.global_variables_initializer())
    n_batches = int(mnist.train.num_examples/batch_size)
    for i in range(n_epochs): # 训练n_epochs次
        

        # 原视频是这个写法，就可以n_epochs的值小一点
        # 我用下面的写法，简单点，但n_epochs需要大一点
        #total_loss = 0
        #for _ in range(n_batches):
        #    X_batch, Y_batch = mnist.train.next_batch(batch_size)
        #    _, loss_batch = sess.run([optimizer, loss], feed_dict={X:X_batch,Y:Y_batch})
        #    total_loss += loss_batch
        #print('average loss epoch {}: {}'.format(i, total_loss/n_batches))

        # 我自己改写，简单点
        X_batch, Y_batch = mnist.train.next_batch(batch_size)
        _, loss_batch = sess.run([optimizer, loss], feed_dict={X:X_batch,Y:Y_batch})

        print('loss epoch {}: {}'.format(i, loss_batch))
    #print('total timie: {} seconds'.format(time.time() - start_time))
    print(sess.run([w,b]))


    # test the model
    n_batches = int(mnist.test.num_examples/batch_size)
    total_correct_preds = 0
    for i in range(n_batches):
        X_batch, Y_batch = mnist.test.next_batch(batch_size) # 真实值
        _, loss_batch, logits_batch = sess.run([optimizer, loss, logits], feed_dict={X:X_batch,Y:Y_batch})
        preds = tf.nn.softmax(logits_batch) # 预测出的值
        correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(Y_batch,1)) # 真实值和预测值比较
        accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))
        total_correct_preds += sess.run(accuracy)
    print('Accuacy {}'.format(total_correct_preds/mnist.test.num_examples))