import numpy as np
import tensorflow as tf
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告

a = tf.placeholder( tf.float32, shape=(3,) ) # 这里shape写 3  (3) 都可以，我还是保持元组定义一致
#print(a.shape)
b = tf.constant([5,5,5], tf.float32)
# a 和 b 有相同的shape
c = a+b   # short for tf.add(a, b)

x = tf.placeholder( tf.float32, shape=(None,2) )
y = tf.constant([[1,1], [2,3]], tf.float32)
yy = tf.Variable( tf.zeros([1,1]))

with tf.Session() as sess:
    #print( sess.run(c) ) # Error 因为a还没有值
    # 正确用法是用字典给a 一个值
    #print( sess.run(c, {a:[1,2,3]}) )  # 这里是用a这个变量作为key，不是'a'字符串
    add = tf.multiply(x, y)

    print( sess.run(add, feed_dict={x: [[2,3],[3,4]]}) )
