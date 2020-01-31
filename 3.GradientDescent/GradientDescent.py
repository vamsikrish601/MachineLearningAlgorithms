# objective is finding the best-fit line using Gradient Descent given X & Y values

import numpy as np

def gradient_descent(x,y):
    # Step 1 --> Start with some values of m & b. Here it is m_current & b_current
    m_curr = b_curr = 0
    # Step 2 --> You have to define how many baby steps that you are going to do. Here it it is 'iterations'.
    iterations = 1000 # trail & error
    # n = len(x) = len(y) assuming x and y length is same
    n = len(x)
    learning_rate = 0.08 # trail & error
    # Step 3 --> Start a for loop with those many baby steps (iterations)
    for i in range(iterations):
        # Calculate y_predicted = m_current * x + b_current
        y_predicted = m_curr * x + b_curr
        # MSE (Cost Function)
        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])
        # Calculate mDerivative and bDerivative such as md and bd here
        md = -(2/n) * sum(x * (y-y_predicted))
        bd = -(2 / n) *sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteration{} ".format(m_curr,b_curr,cost,i))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)

# Last 5 lines from output
# You can observe that the cost is reducing at each of these steps
# m 2.449307050769595, b 1.3778589819185307, cost 0.47927421333200615, iteration995
# m 2.449155141761153, b 1.3784074216500761, cost 0.47895018652693155, iteration996
# m 2.449003284112507, b 1.3789556759562092, cost 0.4786263787892881, iteration997
# m 2.448851477806295, b 1.3795037448996217, cost 0.4783027899709678, iteration998
# m 2.448699722825159, b 1.3800516285429847, cost 0.47797941992396514, iteration999

# How do I know when I should stop to select best-fit line ?

# Keep changing the values of iterations & learning_rate by observing that the output crosses the global minima & output
# should be closer to expected m & b value which is m = 2, b = 3
# iterations = 10000, learning_rate = 0.001 --> This will have reducing cost
# iterations = 10, learning_rate = 0.001 --> This will have reducing cost
# iterations = 10, learning_rate = 0.01 --> This will have reducing cost
# iterations = 10, learning_rate = 0.01 --> This will cross global-minima
# iterations = 10, learning_rate = 0.08 --> This will have reducing cost


# iteratiosn = 1000, learning_rate = 0.08 --> This will help in finding the best-fit line (m & b values)
# You can observe that the difference between the costs is not much
# Now you can use some floating point comparison and pick m & b values when the difference between the costs is
# negligible

# m 2.0000000000008424, b 2.9999999999969553, cost 1.7819635786022613e-24, iteration996
# m 2.000000000000821, b 2.999999999997038, cost 1.687158432784981e-24, iteration997
# m 2.0000000000007976, b 2.9999999999971174, cost 1.5968652558012031e-24, iteration998
# m 2.0000000000007776, b 2.999999999997196, cost 1.5126502520921528e-24, iteration999






