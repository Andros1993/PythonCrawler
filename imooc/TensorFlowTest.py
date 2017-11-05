import tensorflow as tf
import numpy as np

# # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
# x_data = np.float32(np.random.rand(2, 100)) # 随机输入
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
#
# # 构造一个线性模型
# #
# b = tf.Variable(tf.zeros([1]))
# W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
# y = tf.matmul(W, x_data) + b
#
# # 最小化方差
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)
#
# # 初始化变量
# init = tf.initialize_all_variables()
#
# # 启动图 (graph)
# sess = tf.Session()
# sess.run(init)
#
# # 拟合平面
# for step in range(0, 201):
#     sess.run(train)
#     if step % 20 == 0:
#         print (step, sess.run(W), sess.run(b))
#
# # 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]



# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[3., 3.]])

# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[2.]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)
