kf.py is Classic Kalman Filter
akf.py is Adaptive Kalman Filter from kf.py, with more api

search.py is random walk search model
searchWithKF.py is a KF following search model
sigmoidtest.py is Test of curve_fit model
multiSearch.py is for multiple search




**Algorithm 1. Kalman Filter: State Estimation**
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
---


**Algorithm 2. A Step of Multiple Search**
---
Input:

Last Estimation (of x, y axis) outputs: x, y(都加个尖尖角，下标k-1)\[n\];
Last Observation of Acceleration in X, Y, Z axis: (括号换成Z_k);
Current position of Search Boat x0, y0;

Output:

Total Search Time t;

Workflow:

1: State Estimation: Compute New State Outputs y[n](加个尖尖角，下标k) via **Algorithm 1** with Z_k;
2: Find the minimum of distance index: index = argmin(sqrt((y[i](加个尖尖角，下标k) - y0)^2 + (x[i](加个尖尖角，下标k) - x0)^2));
3: Compute speed of Search Boat v_{x0}, v_{y0} via (第三问第二个模型的第一个公式),(第三问第二个模型的第二个公式);
4: Update Position of Search Boat x_0, y_0 via (第三问第二个模型的第三个公式),(第三问第二个模型的第四个公式);
5: if i > Threshold: return failed;
---

