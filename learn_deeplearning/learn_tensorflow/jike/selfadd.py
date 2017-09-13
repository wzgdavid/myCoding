import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告

# 计算1加到10
# 先用正常写法写
sum_ = 0
for n in range(1, 11):
    sum_+=n
print(sum_)

# 用tensorflow方式写，真的很反人类
sum_ = tf.Variable(0, name='sum') 
a = tf.Variable(0, name='1') # 这个a就好比上面那个循环的n
with tf.Session() as sess:
    init  = tf.global_variables_initializer()
    sess.run(init)
    for n in range(1, 11):
        sess.run(a.assign(n))  # 好比 a = n
        assign_sum = sum_.assign( sess.run(tf.add(sum_, a)) ) # sum_ = sum_ + a
        sess.run(assign_sum)   # tf都要run一下才执行
    print( sum_.eval() )       # 打印需要eval方法

