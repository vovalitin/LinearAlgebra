"""

"""
import numpy as np
from numpy import linalg

A = np.array([[4,5],[7,6]])
B = np.array([[-3,10],[1,4]])

# Multiplication matrix
C = A.dot(B)
D = C.dot(A)

# Back matrix inv - invertor
A = np.array([[1,0,0],[1,1,2],[1,1,3]])
C = linalg.inv(A)

# System lin uravnenii
A = np.array([[2,-3],[1,2]])
B = np.array([[3],[5]])

x = linalg.solve(A,B)
