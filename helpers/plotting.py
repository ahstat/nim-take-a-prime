import pandas as pd
import matplotlib.pyplot as plt
from cycler import cycler # for cycle of colors

##########################################
# Simple line plot of the first elements #
##########################################
def line_plot(nimseq, filename,
              xlim = 60, width = 480, height = 350, ppi = 72,
              xlab = 'n (index)', ylab = 'uₙ (value)'):
  figsize = (width/ppi,height/ppi)
  fig = plt.figure(figsize=figsize)
  plt.plot(range(xlim+1), nimseq[:xlim+1], '-', color = 'lightgray', lw = 0.8)
  plt.plot(range(xlim+1), nimseq[:xlim+1], 'o', color = 'black', mfc='none')
  plt.xlim(0, xlim)
  plt.xlabel(xlab)
  plt.ylabel(ylab)
  # ax = plt.axes()
  # ax.spines['top'].set_visible(False)
  # ax.spines['right'].set_visible(False)
  # plt.show()
  fig.savefig(filename, bbox_inches='tight')
  
##############################################################################
# Cumulative proportion along the sequence (of each value) as a stacked plot #
##############################################################################
def cumsum_nim(i, nimseq):
    return 100*(nimseq == i).cumsum() / range(1, len(nimseq)+1)

def cumprop_each_value(nimseq):
    max_val = max(nimseq)
    percent = [cumsum_nim(i, nimseq) for i in range(max_val+1)]
    df = pd.DataFrame(percent).transpose()
    df.columns = [str(i) for i in range(max_val+1)]
    return(df)

def stacked_plot(nimseq, filename,
                 xlim = 5000, width = 1280, height = 1024, ppi = 72,
                 xlab = 'Length of the sequence', ylab = 'Percentages',
                 color = None):
    ##
    # Data frame to plot
    ##
    df = cumprop_each_value(nimseq)
    df = df[:xlim]
    # df.shape # 5000 x 12
    
    ##
    # Colors for each value
    ##
    # color[2] = chartreuse4
    if(color == None):
      color = ['#F25700', '#F8823C', '#458B00', '#65B237',
               '#007EE5', '#00B1DB', '#CC0000', '#DA3540',
               '#F15D5A', '#F27777', '#F3A09E', '#FFDAE1']
    
    ##
    # Plotting
    ##
    # Stacked plots with Pandas: https://stackoverflow.com/questions/44612797
    figsize = (width/ppi,height/ppi)
    fig, ax = plt.subplots(figsize=figsize, linewidth=0)
    # Alternative with anti-aliasing:
    #df.plot.area(figsize=figsize, linewidth=0).get_figure().savefig("out.png")

    ax.set_prop_cycle(cycler('color', color))
    ax.stackplot(df.index, df.values.T, antialiased=False)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    #ax.spines['bottom'].set_visible(False)
    #ax.spines['left'].set_visible(False)

    fig.savefig(filename, bbox_inches='tight')