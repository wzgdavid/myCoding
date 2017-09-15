import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告

#https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650718466&idx=1&sn=016f111001e8354d49dd4ce279d283cd#rd
# 线性模型
x = tf.placeholder(tf.float32, shape=(None, 1) )
W = tf.Variable( tf.zeros([1, 1]) )
b = tf.Variable( tf.zeros([1]) )
y = tf.matmul(x, W) + b

# 成本函数
y_ = tf.placeholder(tf.float32, shape=(None, 1) )
cost = tf.reduce_sum( tf.pow((y_-y), 2) )


# 梯度下降
#有了线性模型、成本函数和数据，我们就可以开始执行梯度下降从而最小化代价函数，以获得 W、b 的「good」值。
#0.00001 是我们每次进行训练时在最陡的梯度方向上所采取的「步」长；它也被称作学习率（learning rate）。
train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(cost)


# 训练模型
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    # 假数据
    for i in range(100):
        xs = np.array([[i]])
        # 简单起见，我们将房价 (ys) 设置成永远是房子面积 (xs) 的 2 倍。
        ys = np.array([[2*i]]) 

        feed = {x:xs, y_:ys}
        sess.run(train_step, feed_dict=feed)
        print(sess.run([W,b]))