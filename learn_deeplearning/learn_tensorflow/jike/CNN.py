'''
卷积神经网络（Convolutional Neural Network，CNN）
http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/mnist_pros.html
教程----深入MNIST
    构建一个多层卷积网络

卷积神经网络有两种神器可以降低参数数目，第一种神器叫做局部感知。
一般认为人对外界的认知是从局部到全局的，而图像的空间联系也是局部的像素联系较为紧密，而距离较远的像素相关性则较弱。
因而，每个神经元其实没有必要对全局图像进行感知，只需要对局部进行感知，
然后在更高层将局部的信息综合起来就得到了全局的信息。网络部分连通的思想，
也是受启发于生物学里面的视觉系统结构。视觉皮层的神经元就是局部接受信息的（即这些神经元只响应某些特定区域的刺激）。


9月24日
这个现在只是把代码拷过来了，还要具体看懂
'''

import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)


# 权重初始化
def weight_variable(shape):
    
    '''
    这个模型中的权重在初始化时应该加入少量的噪声来打破对称性以及避免0梯度。
    '''
    initial = tf.truncated_normal(shape, stddev=0.1) # stddev=0.1 表示噪声
    return tf.Variable(initial)

def bias_variable(shape):
    '''
    由于我们使用的是ReLU神经元，因此比较好的做法是用一个较小的正数来初始化偏置项，
    以避免神经元节点输出恒为0的问题（dead neurons）
    '''
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    '''
    卷积
    '''
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    '''
    池化
    '''
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')


x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

#为了用这一层，我们把x变成一个4d向量，其第2、第3维对应图片的宽、高，
#最后一维代表图片的颜色通道数(因为是灰度图所以这里的通道数为1，如果是rgb彩色图，则为3)。
x_image = tf.reshape(x, [-1,28,28,1])

# 第一层卷积
'''
现在我们可以开始实现第一层了。它由一个卷积接一个max pooling完成。
卷积在每个5x5的patch中算出32个特征。卷积的权重张量形状是[5, 5, 1, 32]，
前两个维度是patch的大小，接着是输入的通道数目，最后是输出的通道数目。 
而对于每一个输出通道都有一个对应的偏置量。
'''
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
'''
We then convolve x_image with the weight tensor, add the bias, 
apply the ReLU function, and finally max pool. 我们把x_image和权值向量进行卷积，
加上偏置项，然后应用ReLU激活函数，最后进行max pooling。
'''
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

#第二层卷积
# 为了构建一个更深的网络，我们会把几个类似的层堆叠起来。第二层中，每个5x5的patch会得到64个特征。
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

'''
密集连接层

现在，图片尺寸减小到7x7，我们加入一个有1024个神经元的全连接层，
用于处理整个图片。我们把池化层输出的张量reshape成一些向量，乘上权重矩阵，加上偏置，然后对其使用ReLU。
'''
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

'''
Dropout

为了减少过拟合，我们在输出层之前加入dropout。
我们用一个placeholder来代表一个神经元的输出在dropout中保持不变的概率。
这样我们可以在训练过程中启用dropout，在测试过程中关闭dropout。 
TensorFlow的tf.nn.dropout操作除了可以屏蔽神经元的输出外，还会自动处理神经元输出值的scale。
所以用dropout的时候可以不用考虑scale。
'''
keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

'''
输出层

最后，我们添加一个softmax层，就像前面的单层softmax regression一样。
'''
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

'''
训练和评估模型

这个模型的效果如何呢？

为了进行训练和评估，我们使用与之前简单的单层SoftMax神经网络模型几乎相同的一套代码，
只是我们会用更加复杂的ADAM优化器来做梯度最速下降，
在feed_dict中加入额外的参数keep_prob来控制dropout比例。然后每100次迭代输出一次日志。
'''

cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(500): # 看下来500次训练好像够了 已经98了，但后面反而会低
        batch = mnist.train.next_batch(50)
        if i%100 == 0:
            train_accuracy = accuracy.eval(feed_dict={
                x:batch[0], y_: batch[1], keep_prob: 1.0})
            print("step %d, training accuracy %g"%(i, train_accuracy))
        train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
    
    print("test accuracy %g"%accuracy.eval(feed_dict={
        x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))