import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'
# Import Valuation Function from Chapter 5
# import sys
# sys.path.append('05_com')

import scipy.stats as scs
def normal_cdf(x):
    # print(norm.cdf(x))
    return scs.norm.cdf(x)

def N_d1(S, K, T, r, q,sigma,sign):
    d1 = (np.log(S / K) + (r - q + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    if sign == 0:
        nd1 = normal_cdf(d1)
        return nd1
    elif sign == 1:
        nd1 = normal_cdf(-d1)
        return nd1



def N_d2(S, K, T, r, q,sigma,sign):
    d2 = (np.log(S / K) + (r - q - (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    if sign == 0:
        nd2 = normal_cdf(d2)
        return nd2
    elif sign == 1:
        nd2 = normal_cdf(-d2)
        return nd2

def BSM_call_value(S, K, T, r, q, sigma):
    call_price = S * np.exp(-q * T) * N_d1(S, K, T, r, q, sigma, 0) - K * np.exp(-r * T) * N_d2(S, K, T, r, q, sigma, 0)
    print("the price of european call option: ", call_price)
    return call_price


# Model and Option Parameters
K = 8000 # strike price
T = 1.0 # time-to-maturity
r = 0.025 # constant, risk-less short rate
vol = 0.2 # constant volatility
# Sample Data Generation
S = np.linspace(4000, 12000, 150) # vector of index level values


h = np.maximum(S - K, 0) # inner value of option
C = [BSM_call_value(S0, K,  T, r, 0, vol) for S0 in S]
# calculate call option values
# Graphical Output
plt.figure()
plt.plot(S, h, 'b-.', lw=2.5, label='inner value')
# plot inner value at maturity
plt.plot(S, C, 'r', lw=2.5, label='present value')
# plot option present value
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('index level $S_0$')
plt.ylabel('present value $C(t=0)$')
plt.show()
