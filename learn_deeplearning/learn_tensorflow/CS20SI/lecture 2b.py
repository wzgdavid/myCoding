import numpy as np
import tensorflow as tf
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告

'''
Eval() a variable
'''
#W = tf.Variable(tf.truncated_normal([700, 10]))
#with tf.Session() as sess:
#    sess.run(W.initializer)
#    print(W.eval())


'''
tf.Variable.assign()
'''
#W = tf.Variable(10)
#W.assign(100)  # 只是返回一个assign的操作，还没run过
##with tf.Session() as sess:
##    sess.run(W.initializer)
##    print(W.eval())  # 还是10， 因为那个assign还没有run过
#
## 要返回100， 这样改
#with tf.Session() as sess:
#    #sess.run(W.initializer) # 其实这步可以不用写
#    sess.run(W.assign(100))
#    print(W.eval())  # 100

#a = tf.Variable(2)
#b = a.assign(2*a) # assign 会更新对象的值
#with tf.Session() as sess:
#    sess.run(a.initializer)
#    print(a.eval(), b.eval()) # 2 4
#    sess.run(b)
#    print(a.eval(), b.eval()) # 8 16
#    sess.run(b)
#    print(a.eval(), b.eval()) # 32 64

#a = tf.Variable(10)
#with tf.Session() as sess:
#    sess.run(a.initializer)
#    print(a.eval()) # 10
#    sess.run(a.assign_add(10))  # 不想更新，用assign_add,assign_sub等方法
#    print(a.eval()) # 20
#    sess.run(a.assign_sub(5))
#    print(a.eval()) # 15

'''
每个session都有一份variable的拷贝, 他们的变量独立
'''
#a = tf.Variable(10)
#s1 = tf.Session()
#s2 = tf.Session()
#s1.run(a.initializer)
#s2.run(a.initializer)
#print(s1.run(a.assign_add(10))) # 20
#print(s2.run(a.assign_add(2)))  # 12

'''
用一个variable 去initialize另一个variable
'''
# 这种方法必须确保w的initialize在u之前
#w = tf.Variable(tf.truncated_normal([700, 10]))
#u = tf.Variable(2*w)
#s = tf.InteractiveSession()
#s.run(w.initializer)
#s.run(u.initializer)
#print(w.eval())
#print(u.eval())

'''
运行顺序依赖
'''
#with g.control_dependencies([a, b, c]):
#    # 假设g里有5个 操作
#    # d 和 e 只有在a, b, c执行过产能执行
#    d = ...
#    e = ...#

'''              Placeholders
tensorflow程序一般有两步
1  assemble a graph
2  use a session to execute operations in the graph

=> can assemble the graph first without knowing the values needed for computation

analogy:
can define the function f(x, y) = x*2+y without knowing value of x or y,
x, y are placeholders for the actual values.
这和我们初中学的函数一样，定义函数时不需要知道具体的x，或y
'''
'''
tf.placeholder(dtype, shape=None, name=None)
'''
a = tf.placeholder( tf.float32, shape=(3,) ) # 这里shape写 3  (3) 都可以，我还是保持元组定义一致
#print(a.shape)
b = tf.constant([5,5,5], tf.float32)
# a 和 b 有相同的shape
c = a+b   # short for tf.add(a, b)

with tf.Session() as sess:
    #print( sess.run(c) ) # Error 因为a还没有值
    # 正确用法是用字典给a 一个值
    print( sess.run(c, {a:[1,2,3]}) )  # 这里是用a这个变量作为key，不是'a'字符串


#tf.Graph.is_feedable(tersor)

'''
Feeding values to TF op
'''
a = tf.add(2, 4)
b = tf.multiply(a, 3)
with tf.Session() as sess:
    replace_dict = {a: 15}
    print( sess.run(b ) )   # 18
    print( sess.run(b, feed_dict=replace_dict) ) # 45

'''
Lazy loading Example
'''
# no Lazy loading:
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
z = tf.add(x, y)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #x.assign(10)
    #y.assign(4)
    writer = tf.summary.FileWriter('./graphs',sess.graph)
    for _ in range(10):
        sess.run(z)
#writer.close()

#  Lazy loading:
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
with tf.Session() as sess:
    sess.run( tf.global_variables_initializer() )
    
    for _ in range(10):
        sess.run( tf.add(x, y) ) # 在run的时候去load x和y
    writer = tf.summary.FileWriter('./graphs',sess.graph)
#writer.close()
print( tf.get_default_graph().as_graph_def() )

'''
One of the most common TF non-bug bugs I've seen on Github
                  Solution
1  Separate definition of ops form compution/running ops
2  Use python property to ensure function is also loaded once
   the first time it is called*
'''
