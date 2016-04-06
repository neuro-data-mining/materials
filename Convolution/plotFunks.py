import matplotlib.pyplot as plt

# A Whole Bunch of Convenience Functions for Cleaning Up Plots
def removeAxes(ax):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

def removeFrames(ax,sides=['top','right']):
    for side in sides:
        ax.spines[side].set_visible(False)

def removeTicks(ax,axes):
    if 'x' in axes:
        ax.tick_params(axis='x',
                        which='both',
                        top='off',
                        labeltop='off',
                        bottom='off',
                        labelbottom='off')
    if 'y' in axes:
        ax.tick_params(axis='y',
                        which='both',
                        left='off',
                        labelleft='off',
                        right='off',
                        labelright='off')

def addAxis(ax,axis='horizontal'):
    if axis == 'horizontal':
        xmin,xmax = ax.get_xlim()
        ax.hlines(0,xmin,xmax)
    elif axis == 'vertical':
        ymin,ymax = ax.get_ylim()
        ax.vlines(0,ymin,ymax)

def cleanPlot(ax):
    removeFrames(plt.gca(),['top','right','bottom']);
    removeTicks(plt.gca(),['x','y']);

def setLims(ax,xBounds,yBounds):
    ax.set_xlim(xBounds); ax.set_ylim(yBounds);
