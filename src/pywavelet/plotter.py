import math
import numpy as np
import matplotlib.pyplot as plt

def power_plotter(ax, time, periods, values, levels, **kwargs):
    img = ax.contourf(time, 
                      np.log2(periods), 
                      np.log2(np.abs(values)), 
                      np.log2(levels), 
                      cmap='jet')
    ax.set(**kwargs)
    
    # Default settings for ticks and labels
    # create yticks
    yt = np.arange(0,np.log2(periods[-1]))
    ylabels = (2 ** yt)
    ax.set_yticks(yt)
    ax.set_yticklabels(ylabels)
    # create colobars
    cbar_ticks = np.arange(np.log2(levels[0]),np.log2(levels[-1]),step=2)
    cbar_labels = ['{:4.2E}'.format(ct) for ct in (2 ** cbar_ticks)]
    cbar = plt.colorbar(img, ax=ax, shrink=0.9)
    cbar.set_label('Power')
    cbar.set_ticks(cbar_ticks)
    cbar.set_ticklabels(cbar_labels)
    ax.invert_yaxis()
    
    return img

def coi_plotter(ax, time, coi, periods, **kwargs):
    artists = []
    # test coi plotting
    coi_p = time[0] + coi[coi + time[0] <= time[-1]]
    coi_b = time[-1] - coi[coi + time[0] <= time[-1]]

    # find the common coi line
    artists.append(ax.fill_between(coi_p, np.log2(periods[:coi_p.size]), 
                                   np.log2(periods[-1]), **kwargs))
    artists.append(ax.fill_between(coi_b, np.log2(periods[:coi_p.size]), 
                                   np.log2(periods[-1]), **kwargs))
    return artists

def levels(val, val_min=None, val_max=None):
    lev = []
    if val_min is None:
        val_min = val.min()
    if val_max is None:
        val_max = val.max()
    for i in range(math.ceil(np.log2(val_max / val_min))):
        val_min = val_min * 2
        lev.append(val_min)
    return lev
