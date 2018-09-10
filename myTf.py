# -*- coding:utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
"""
Tensorflow基本的使用
"""
m1 = tf.constant([[3, 3]])
m2 = tf.constant([[2], [3]])

product = tf.matmul(m1, m2)
# 定义一个回话, 启动默认图
# 方式一
sess1 = tf.Session()
result = sess1.run(product)
print(result)
sess1.close()

# 方式二
with tf.Session() as sess2:
    result2 = sess2.run(product)
    print(result2)