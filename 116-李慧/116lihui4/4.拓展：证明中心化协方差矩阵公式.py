# 4.证明中心化协方差矩阵公式

import numpy as np

# 创建一个样本矩阵
X = np.array([[-1,2,66,-1], [-2,6,58,-1], [-3,8,45,-2], [1,9,36,1], [2,10,62,1], [3,5,83,2]])

# 计算均值向量
mean_vector = np.mean(X, axis=0)

# 中心化样本矩阵
X_centered = X - mean_vector

# 计算中心化后的协方差矩阵
cov_matrix_centered = np.cov(X_centered, rowvar=False)

print("中心化后的协方差矩阵：")
print(cov_matrix_centered)

# 计算协方差矩阵的公式
n_samples = X.shape[0]
cov_matrix_formula = np.dot(X_centered.T, X_centered) / (n_samples - 1)

print("\n协方差矩阵的公式计算结果：")
print(cov_matrix_formula)