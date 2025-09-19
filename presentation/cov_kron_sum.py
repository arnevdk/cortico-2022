import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from viz import plot_cov_disp

emp_cov = np.load('data/emp_cov.npy')
emp_prec = np.load('data/emp_prec.npy')
sum_cov = np.load('data/sum_cov.npy')
sp_covs = np.load('data/sp_covs.npy')
tmp_covs = np.load('data/tmp_covs.npy')
sp_precs = np.load('data/sp_precs.npy')
tmp_precs = np.load('data/tmp_precs.npy')
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
plot_cov_disp(emp_cov, ax)
fig.tight_layout()
fig.savefig('figures/emp_cov.png', format='png')
fig, ax = plt.subplots(1, 1, figsize=(6, 6))

plot_cov_disp(emp_prec, ax)
fig.tight_layout()
fig.savefig('figures/emp_prec.png', format='png')

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
plot_cov_disp(emp_cov, ax)
ax.set_xlabel('Time × space (channels ∗ samples)')
ax.set_ylabel('Time × space (channels ∗ samples)')
fig.tight_layout()
fig.savefig('figures/emp_cov_label.png', format='png')

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
plot_cov_disp(emp_prec, ax)
ax.set_xlabel('Time × space (channels ∗ samples)')
ax.set_ylabel('Time × space (channels ∗ samples)')
fig.tight_layout()
fig.savefig('figures/emp_prec_label.png', format='png')

fig, ax = plt.subplots(1, 1, figsize=(6, 6))
plot_cov_disp(sum_cov, ax)
fig.tight_layout()
fig.savefig('figures/sum_cov.png', format='png')

for c in range(3):
    fig, ax = plt.subplots(1,1, figsize=(4,4))
    plot_cov_disp(sp_covs[c], ax)
    fig.tight_layout()
    fig.savefig(f'figures/sp_cov_{c+1}.png', format='png')
    fig, ax = plt.subplots(1,1, figsize=(4,4))
    plot_cov_disp(tmp_covs[c], ax)
    fig.tight_layout()
    fig.savefig(f'figures/tmp_cov_{c+1}.png', format='png')
    fig, ax = plt.subplots(1,1, figsize=(4,4))
    plot_cov_disp(sp_precs[c], ax)
    fig.tight_layout()
    fig.savefig(f'figures/sp_prec_{c+1}.png', format='png')
    fig, ax = plt.subplots(1,1, figsize=(4,4))
    plot_cov_disp(tmp_precs[c], ax)
    fig.tight_layout()
    fig.savefig(f'figures/tmp_prec_{c+1}.png', format='png')

struct_prec = np.kron(sp_precs[2], tmp_precs[2])
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
plot_cov_disp(struct_prec, ax)
fig.tight_layout()
fig.savefig('figures/struct_prec.png', format='png')