import numpy as np
import tensorflow as tf
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告


a = tf.add(3, 5)
b = tf.multiply(5, 5)
c = tf.add(a, b)
with tf.Session() as s:
    print(s.run(c))


x = 2
y = 1
op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
op3 = tf.pow(op1, op2)
with tf.Session() as sess:
    print(sess.run(op3))


x = 2
y = 1
op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
useless = tf.multiply(x, op1)
op3 = tf.pow(op1, op2)
with tf.Session() as sess:
    print(sess.run(op3))


x = 2
y = 1
op1 = tf.add(x, y)
print(op1)
op2 = tf.multiply(x, y)
useless = tf.multiply(x, op1)
op3 = tf.pow(op1, op2)
with tf.Session() as sess:
    # 可以用run同时运算几个结果，需要运行的Tensor对象放在一个list中
    print( sess.run([op3, useless]) ) 
    #以上那一句等于
    #sess.run(op3)
    #sess.run(useless)
    


a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], name='a')
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], name='b')
c = tf.matmul(a, b)   # 矩阵相乘
sess = tf.Session()
print(sess.run(c))


a = tf.constant( np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]] ), name='a')
b = tf.constant( np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]] ), name='b')
c = tf.matmul(a, b)   # 矩阵相乘
sess = tf.Session()
print(sess.run(c))

#另外定义一个graph最为默认的话，Session要传一个graph参数
g = tf.Graph()
with g.as_default(): # 这个add操作是在自定义的graph  g里操作
    x = tf.add(3,5)
# 因为下面x是定义在graph g 里的，所以session的参数要指定graph
with tf.Session(graph=g) as s: 
    print(s.run(x))

g = tf.Graph()
a = tf.constant(4)  # 这个操作加到默认的graph里了
with g.as_default():
    b = tf.constant(5) # 这个操作加到自定义的graph g里了

g1 = tf.get_default_graph()
g2 = tf.Graph()
with g1.as_default():
    a = tf.constant(3) # 这个操作加到默认的graph里了
with g2.as_default():
    a = tf.constant(5) # 这个操作加到自定义的graph g1里了