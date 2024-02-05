kf.py is Classic Kalman Filter
akf.py is Adaptive Kalman Filter from kf.py, with more api

search.py is random walk search model
searchWithKF.py is a KF following search model
sigmoidtest.py is Test of curve_fit model
multiSearch.py is for multiple search


Kalman Filter:

Algorithm:
---
Input:

Last Estimation output: (括号换成x后验，下标k-1);
Last Observation of Acceleration in X, Y, Z axis: (括号换成Z_k);

Output:

New Estimation output: (括号换成x后验，下标k);

Workflow:

1: State Propagation: Compute x_k^- via(公式序号), Compute P_k^- via(公式序号);
2: State Esimation: When Observation Z_k comes:
3:      Compute Kalman Gains K via(公式序号);
4:      Compute Updated State \hat{x_k} via(公式序号)
5:      Compute Updated Covariance \hat{P_k} 
