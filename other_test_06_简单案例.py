﻿import tensorflow as tf
import numpy as np


# 使用numpy生成100个随机点
x_data = np.random.rand(100)
# 这是一条 y = kx + b 的直线条
y_data = x_data*0.1 + 0.2

# 构造一个线性模型:k = 0，b = 0  (k b 值是任意的，偏差越大，需要训练的次数就越多)
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k * x_data + b

# 二次代价函数
loss = tf.reduce_mean(tf.square(y_data - y))
# 定义一个梯度下降法来进行训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
# 最小化代价函数
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # 打印初始值 k = 0，b = 0
    print(sess.run(k), sess.run(b))
    for step in range(201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(k), sess.run(b))




