import numpy as np
import random
import matplotlib.pyplot as plt


def generate_random(args, MIN, MAX, N):

    if args.mode == "normal":
        mu, sigma = 5, 1
        s = np.random.normal(mu, sigma, N)
        s = np.round(s)
        s = np.clip(s, MIN, MAX)

        """
        # 畫出資料的直方圖
        count, bins, ignored = plt.hist(s, 30, density=True)

        # 繪製常態分布的機率密度函數
        plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                 np.exp(- (bins - mu)**2 / (2 * sigma**2)),
                 linewidth=2, color='r')
        plt.show()
        """

    elif args.mode == "uniform":
        s = [random.uniform(MIN, MAX) for _ in range(N)]
        s = np.round(s)
        s = np.clip(s, MIN, MAX)

    elif args.mode == "right":
        s = np.random.exponential(scale=1, size=1000)
        alpha = 2
        beta = 5
        t = np.random.beta(alpha, beta, 1000)

        # 將兩個分布組合起來
        s = s * t * 3 + 1
        s = np.round(s)
        s = np.clip(s, MIN, MAX)

        plt.hist(s, bins=50, density=True, alpha=0.7)
        plt.show()

    elif args.mode == "left":
        s = np.random.beta(1, 4, size=1000)
        s = MAX - s*8 + 1
        s = np.round(s)
        s = np.clip(s, MIN, MAX)

        plt.hist(s, bins=50, density=True, alpha=0.7)
        plt.show()

    return s
