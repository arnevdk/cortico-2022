import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.linewidth'] = 2
plt.rcParams['font.size'] = 18

def plot_evoked_image_disp(evoked, ax,                          **kwargs):
    kwargs.setdefault('scalings', dict(eeg=1))
    kwargs.setdefault('show', False)
    kwargs.setdefault('show_names', False)
    kwargs.setdefault('colorbar', False)
    kwargs['axes'] = ax

    evoked.nave = None
    evoked.plot_image(**kwargs)

    ax.tick_params(axis='both', top=False, bottom=False, left=False, right=False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title('')
    ax.set_xlabel('Time (samples)')
    ax.set_ylabel('Space (channels)')
    #ax.axvline(0, color='black', linewidth=2)

    return ax

def plot_cov_disp(data, ax, **kwargs):
    data = np.flip(data, axis=1)
    opt = np.max(np.abs(data))
    kwargs.setdefault('vmin', -opt)
    kwargs.setdefault('vmax', opt)
    im = ax.pcolormesh(data, cmap='BrBG', **kwargs)
    ax.set_aspect('equal')
    ax.tick_params(left=False,
                   bottom=False,
                   labelleft=False,
                   labelbottom=False)
    return ax

def plot_bar_disp(data, ax, **kwargs):
    ax.bar(np.arange(len(data)), data)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(left=False,
                   bottom=False,
                   labelleft=False,
                   labelbottom=False)