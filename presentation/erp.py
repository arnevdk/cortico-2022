import mne
import os
from mne_bids import BIDSPath
from mne.channels import find_layout
from mne import combine_evoked
from viz import plot_evoked_image_disp
import matplotlib.pyplot as plt

bids_root = os.path.join(mne.get_config('MNE_DATA'), 'derivatives',
                         'mne-bids-pipeline', 'MDA-KUL_COMPNEURO_P3')
path = BIDSPath(root=bids_root, task='P3', datatype='eeg', processing='clean',
                suffix='epo', check=False)

diff_evokeds = []
for subject_paths in path.match():
    epochs = mne.read_epochs(subject_paths)
    epochs.drop_channels(['TP9', 'TP10'])
    epochs.crop(tmin=0, tmax=1.0)
    epochs.pick_types(eeg=True, eog=False)
    layout = find_layout(epochs.info)
    pos = dict()
    for ch in epochs.ch_names:
        if ch in layout.names:
            layout_ch_idx = layout.names.index(ch)
            pos[ch] = 1 - layout.pos[layout_ch_idx, 1]
        else:
            pos[ch] = 0
    ch_order = sorted(epochs.ch_names, key=lambda ch: pos[ch])
    epochs.reorder_channels(ch_order)

    target_evoked = epochs['stimulus/target'].average()
    non_target_evoked = epochs['stimulus/non-target'].average()
    diff_evoked = combine_evoked([target_evoked, non_target_evoked],
                                 weights=[1, -1])
    diff_evokeds.append(diff_evoked)
grand_avg_diff_evoked = combine_evoked(diff_evokeds, weights='equal')
fig, ax = plt.subplots(1,1)
fig.tight_layout()
plot_evoked_image_disp(grand_avg_diff_evoked, ax)
fig.savefig('figures/grand_avg.eps', format='eps')
fig.show()