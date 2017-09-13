import numpy as np
import tensorflow as tf
import os  
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # 让它别出警告

#a = tf.constant(2, name='2') # name  指在图中的名字
#b = tf.constant(3, name='3')
#x = tf.add(a, b, name='myadd') # name 不能有空格
#with tf.Session() as sess:
#    # 运行一下这个代码，这一步把图画好了，在graphs在产生了一个文件
#    # 然后cmd中键入tensorboard --logdir="./graphs" --port=6006
#    # 访问localhost:6006, 选graphs标签，可看到这个图
#    writer = tf.summary.FileWriter('./graphs', sess.graph)
#writer.close()



## 如果有多个图，这里画其中一个
#g1 = tf.get_default_graph()
#g2 = tf.Graph()
#with g1.as_default():
#    a = tf.constant(3) # 这个操作加到默认的graph里了
#with g2.as_default():
#    a = tf.constant(2, name='2')
#    b = tf.constant(3, name='3')
#    x = tf.add(a, b)
#with tf.Session(graph=g2) as sess:
#    writer = tf.summary.FileWriter('./graphs', sess.graph)
#writer.close()


'''
关于参数 tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
verify_shape=False时，不检查参数的shape，
如果这样调用
a = tf.constant(1, shape=(2,2))
实际这个a的值是个(2,2)shape值为1的ndarray
[[1 1]
 [1 1]]  
可以这样查看
tf.InteractiveSession()  # 没有这一步，a不能调eval方法
a.eval()

如果是这样a = tf.constant([1,2,3], shape=(3,3))
返回
[[1 2 3]
 [3 3 3]
 [3 3 3]]
如果value参数是容器，可以看到它只是重复value参数里元素的最后一个值

但verify_shape=True
a = tf.constant(1, shape=(2,2), verify_shape=True)
返回错误
'''

#a = tf.constant([1,2,3], shape=(3,3))
tf.InteractiveSession()  # variable 的 eval() 不用这句
#print(a.eval())

#a = tf.constant([2, 2], name='a')
#b = tf.constant( [(0,1),(2,3)], name='b')
#c = tf.constant( [[2, 2],[2, 2]], name='c')
#x = tf.add(a, b, name='add')  # a,b的shape不同，但能相加，相加时会广播,就像numpy一样，如下示例
##a = np.array([1,2])  # 在运算时 a 其实是 [(1,2),(1,2)]
##b = np.array([(0,1),(2,3)])
##print(a+b)
#y = tf.multiply(a, b, name='mul')   # 这个只是相乘，就是矩阵对应位置的元素相乘
#z = tf.matmul(c, b, name='matmul')  # 这个是矩阵乘
#with tf.Session() as sess:
#    x, y = sess.run( [x, y] )
#    print(y)
#    z = sess.run(z)
#    print(z)
#with tf.Session() as sess:
#    writer = tf.summary.FileWriter('./graphs', sess.graph)
#writer.close()

'''
Tensors filled with a specific value
'''
#tf.zeros(shape, dtype=tf.float32, name=None)  和 numpy.zeros 类似
#tf.zeros_like(input_tensor, dtype=None, name=None) 和 numpy.zeros_like 类似
#zl = tf.zeros_like([[1],[2],[3]]) # 根据zeros_like的参数的shape，返回一个zeros
#print(zl.eval())
#输出[[0]
#     [0]
#     [0]]
# ones 和 ones_like 与上面一样

#填充其他值
#tf.fill([2,3], 8) ===> [[8,8,8],[8,8,8]]
# 在numpy中同样功能，建一个array，然后fill

# tensor对象不可迭代
#a = tf.linspace(10.0 ,13.0, 4)
#b = tf.range(3,18,3) # 和range类似
#print(b.eval())

# 一些random的方法  先略

'''
Operations
'''
#a = tf.constant( [3,6] )
#b = tf.constant( [2,2] )
#tf.add(a, b) # [5 8]
#tf.add_n([a, b, b]) # a+b+b
#tf.multiply(a, b)  # [6  12]
##tf.matmul(a, b)    # ValueError
#tf.matmul( tf.reshape(a, [1, 2]), tf.reshape(b, [2, 1]) )    #  [[18]]
#tf.div(a, b) # [1 3]  除法
#tf.mod(a, b) # [1 0]  取余数

'''
Tensorflow Data types
'''
# 0-d tensor, 标量，就是我们的数字
t0 = 19  
#print( tf.zeros_like(t0).eval() )   # 0
#print( tf.ones_like(t0).eval() ) 

# 1-d tensor, vector 向量
#t1 = ['apple','peach', 'banana']
#print( tf.zeros_like(t1).eval() )   # [b'' b'' b'']
#print( tf.ones_like(t1).eval() )    # 报错

t1 = [1,2, 3] # 看来这些like函数的返回和t1元素的类型有关
#print( tf.zeros_like(t1).eval() )   # [b'' b'' b'']
#print( tf.ones_like(t1).eval() ) 
#看到31:24 https://www.bilibili.com/video/av10790020/index_1.html#page=2

# 2-d tensor  matrix 矩阵
t2 = [[True, False, False],
      [True, False, False],
      [True, False, False]]
#print( tf.zeros_like(t2).eval() )
##返回值[[False False False] 
## [False False False]
## [False False False]]
#print( tf.ones_like(t2).eval() )
##返回值[[ True  True  True] # 
## [ True  True  True]
## [ True  True  True]]

'''
TF vs numpy Data Types
'''
#tf.int32 == np.int32 # True
#tf.ones([2,2], np.float32)

'''
Variables?
'''
a = tf.Variable(2, name='scalar')
b = tf.Variable([2, 3], name='vector')
c = tf.Variable([[1,2], [3,4]], name='matrix')
W = tf.Variable(tf.zeros([784,10]))

# Variable 对象方法
#x = tf.Variable()
#x.initializer
#x.value() # read op
#x.assign(...) # write op
#x.assign_add(...) # and more

# 必须initialize你的variables
#init  = tf.global_variables_initializer()
#with tf.Session() as sess:
#    sess.run(init)
#    writer = tf.summary.FileWriter('./graphs', sess.graph)
#writer.close()

# initialize 部分variable
init_ab = tf.variables_initializer([a, b], name='init_ab')
with tf.Session() as sess:
    sess.run(init_ab)
# initialize 一个variable
W = tf.Variable(tf.zeros([784, 10]))
with tf.Session() as sess:
    sess.run(W.initializer)
