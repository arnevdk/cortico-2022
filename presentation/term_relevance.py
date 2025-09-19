import numpy as np
import matplotlib.pyplot as plt

from viz import plot_bar_disp

term_relevance = np.load('data/term_relevances.npy')
fig, ax = plt.subplots(1,1)
ax.set_xlabel('Covariance term')
ax.set_ylabel('Scale (λ)')
plot_bar_disp(term_relevance, ax)
fig.savefig('figures/term_relevance.eps', format='eps')