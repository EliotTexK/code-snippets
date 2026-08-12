import matplotlib.pyplot as plt
import numpy as np

# dummy data for graphing
X = np.linspace(start=0,stop=67,num=10)
Y1 = X * X
Y2 = X * 0.25
Y3 = np.full_like(X, fill_value=67)
Y4 = np.sin(X)


# 1 row, 2 columns (Side-by-side)
fig, axs = plt.subplots(1, 2)
axs[0].plot(X, Y1) # Left plot
axs[1].plot(X, Y2) # Right plot

# 2 rows, 2 columns
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(X, Y1) # Top-left
axs[0, 1].plot(X, Y2) # Top-right
axs[1, 0].plot(X, Y3) # Bottom-left
axs[1, 1].plot(X, Y4) # Bottom-right

# Shared X-axis (domain) between multiple graphs
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Shared Y-axis (range) between multiple graphs
# Just use sharey instead of sharex

# Titles for subplots
axs[0, 0].set_title("low σ, low ℓ")
axs[0, 1].set_title("low σ, high ℓ")
axs[1, 0].set_title("low σ, low ℓ")
axs[1, 1].set_title("high σ, low ℓ")

# Vertical/Horizontal gap between subplots
fig.subplots_adjust(hspace=0.1, vspace=0.2)
