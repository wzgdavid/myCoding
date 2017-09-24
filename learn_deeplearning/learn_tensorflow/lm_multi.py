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
cost = tf.reduce_mean( tf.pow((y_-y), 2) )   # 也叫loss 损失

train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(cost)

init = tf.global_variables_initializer()
# 训练模型
with tf.Session() as sess:
    sess.run(init)
    
    for i in range(80):
        # 假数据
        xs = np.array([[i,i]])
        # 简单起见，我们将房价 (ys) 设置成永远是房子面积 (xs) 的 2 倍。
        ys = np.array([[3*i + 2*i]]) 

        feed = {x:xs, y_:ys}
        #sess.run(train_step, feed_dict=feed)
        
        # cs20si 中的写法， 打印损失
        _, c = sess.run([train_step, cost], feed_dict=feed)
        print('epoch {}: {}'.format(i, c)) # 可以看到损失，可以选比较好的循环次数
    print(sess.run([W,b]))