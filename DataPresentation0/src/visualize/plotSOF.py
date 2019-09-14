#contents:
#  pplot_dev_vs_df(df_notds, df_ds, title_text, xlimit, ylabel_text):
#  plot_2col(df_notds, df_ds, title_text, xlimit, xlabel_text, ylabel_text, ptype)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# some simple plotting scripts to plot Data Scientists vs. non-Data Scientists
def plot_notds_vs_ds(df_notds, df_ds, title_text, xlimit, ylabel_text):
    """
    Generate a simple pair of side by side plots

    Parameters
    ----------
    df_notds : Series holding non DS data
        xxx

    df_ds : dataframe
        xxx

    title_text : string
        Super-title content

    x_limit : xx
        xx.

    y_label_text : x
        xx

    hardcoded : also SOURCE_TEXT
    """
    fig = plt.figure(figsize=(15, 12))
    grid_size = (10, 10)  # lets space stuff out...
    SOURCE_TEXT = 'Source: StackOverFlow Dev survey, 2019'

    #title_text = 'language LOVE (use now AND want to use it next year'
    #xlimit = {0,95} #

    xlabel_text = 'Incidence (pct)'

    # Place A Title On The Figure
    fig.text(x=0.995, y=0.02, s=SOURCE_TEXT, verticalalignment='bottom',
             rotation='vertical', color='#524939')
    # Overlay multiple plots onto the same axis, which spans 1 entire column of the figure
    tall_left_ax = plt.subplot2grid(grid_size, (1, 1), colspan=3, rowspan=9)
    tall_right_ax = plt.subplot2grid(grid_size, (1, 6), colspan=3, rowspan=9)
    #ax1 = lang_pct.plot.barh(ax=tall_left_ax,legend=False, title='All Respondents',label='xxx',x='string',y='lang')
    ax1 = df_notds.plot.barh(ax=tall_left_ax,
                           legend=False,
                           title='non-Data Scientists').set(xlabel=xlabel_text, ylabel=ylabel_text, xlim=xlimit)
    ax2 = df_ds.plot.barh(ax=tall_right_ax,
                          legend=False,
                          title='Data Scientists').set(xlabel=xlabel_text, xlim=xlimit)
    # plt.tight_layout()
    plt.suptitle(title_text, fontsize=22)
    # should also move the ylabels to the right side for the second plot...

def plot_2col(df_notds, df_ds, title_text, xlimit, xlabel_text, ylabel_text, ptype):

    fig = plt.figure(figsize=(15, 12))
    grid_size = (10, 10)  # lets space stuff out...
    SOURCE_TEXT = 'Source: StackOverFlow Dev survey, 2019'

    # Place A Title On The Figure
    fig.text(x=0.995, y=0.02, s=SOURCE_TEXT, verticalalignment='bottom',
             rotation='vertical', color='#524939')
    # Overlay multiple plots onto the same axis, which spans 1 entire column of the figure
    tall_left_ax = plt.subplot2grid(grid_size, (1, 1), colspan=3, rowspan=9)
    tall_right_ax = plt.subplot2grid(grid_size, (1, 6), colspan=3, rowspan=9)

    if ptype == 'barh':
        #ax1 = lang_pct.plot.barh(ax=tall_left_ax,legend=False, title='All Respondents',label='xxx',x='string',y='lang')
        ax1 = df_notds.plot.barh(ax=tall_left_ax,
                               legend=False, title='non-Data Scientists').set(xlabel=xlabel_text,
                                                                     ylabel=ylabel_text,
                                                                     xlim=xlimit)
        ax2 = df_ds.plot.barh(ax=tall_right_ax,
                              legend=False,
                              title='Data Scientists').set(xlabel=xlabel_text,
                                                           xlim=xlimit)
    elif ptype == 'pie':

        #ax1 = lang_pct.plot.barh(ax=tall_left_ax,legend=False, title='All Respondents',label='xxx',x='string',y='lang')
        ax1 = df_notds.plot.pie(
            ax=tall_left_ax, legend=False, title='non-Data Scientists')
        ax2 = df_ds.plot.pie(ax=tall_right_ax, legend=False,
                             title='Data Scientists')

    elif ptype == 'hist':
        nbins = 25
        xlimit = list(xlimit)
        binz = np.arange(xlimit[0], xlimit[1], np.ceil((xlimit[1]-xlimit[0])/nbins) )
        ax1 = df_notds.plot.hist(density=True, color='blue',
                        bins=binz, alpha=.3,
                        ax=tall_left_ax, legend=False, title='non-Data Scientists')
        ax2 = df_ds.plot.hist(density=True, color='red',
                        bins=binz, alpha=.3,
                        ax=tall_right_ax, legend=False, title='Data Scientists')
        
    else:
        ax1 = lang_pct.plot.bar(ax=tall_left_ax, legend=False,
                                title='All Respondents', label='xxx', x='string', y='lang')
        ax1 = df_notds.plot.bar(ax=tall_left_ax,
                              legend=False, title='non-Data Scientists').set(xlabel=xlabel_text,
                                                                    ylabel=ylabel_text,
                                                                    xlim=xlimit)
        ax2 = df_ds.plot.bar(ax=tall_right_ax,
                             legend=False,
                             title='Data Scientists').set(xlabel=xlabel_text,
                                                          xlim=xlimit)

    tall_right_ax.yaxis.tick_right()
    # plt.tight_layout()
    plt.suptitle(title_text, fontsize=22)
    # should also move the ylabels to the right side for the second plot...

    # def plot_axis(ax, series, title):
#     labels = [shorten(s, width=30, placeholder='...') for s in series.index]
#     y_pos = np.arange(len(series))
#     ax.barh(y_pos, series)
#     ax.set_yticks(y_pos)
#     ax.set_yticklabels(labels, minor=False)
#     ax.set_title(title)
#     ax.xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))


# def plot_ranking(dataframe, tech, figsize=(18, 12), min_worked_with=1000):
#     columns = [f'{tech}_{col}' for col in ['worked_with', 'liked', 'new']]

#     annotation = '''Graphs 1 & 2 show the percentage of respondents who named the {} relative to how many respondents answered the corresponding question. The 3rd graph shows how many of those who worked
# with the {} want to continue to do so. Data: kaggle.com/stackoverflow/stack-overflow-2018-developer-survey • Author: Ramiro Gómez - ramiro.org'''.format(tech, tech, tech)

#     # Only count responses with at least one answer to the questions related to this technology
#     response_count = len(dataframe[columns].replace(to_replace=set(), value=np.nan).dropna(how='all'))

#     counters = [Counter(chain.from_iterable(dataframe[col].apply(list))) for col in columns]
#     df = pd.DataFrame(counters, index=columns).T.sort_values(f'{tech}_worked_with')
#     # Limit to technologies worked with by at least min_worked_with respondents
#     df = df[df[f'{tech}_worked_with'] >= min_worked_with]

#     worked_with = (df[f'{tech}_worked_with'] / response_count).sort_values()
#     liked = (df[f'{tech}_liked'] / df[f'{tech}_worked_with']).sort_values()
#     new = (df[f'{tech}_new'] / response_count).sort_values()

#     fig, axes = plt.subplots(nrows=1, ncols=3, figsize=figsize)
#     fig.suptitle('Stack Overflow Survey 2018: {} Preferences'.format(tech.title()), y=0.94, size=25)
#     fig.subplots_adjust(wspace=0.5)

#     plot_axis(axes[0], worked_with, 'Worked with')
#     plot_axis(axes[1], new, 'Not worked with but desired')
#     plot_axis(axes[2], liked, 'Worked with and desired')

#     plt.annotate(annotation, xy=(5, 30), xycoords='figure pixels', size=12)


# plot_ranking(df_tech, 'language')


def plot_quantiles(df_1, df_2,ylabel_text,title_text): #, xlimit, xlabel_text, ylabel_text, ptype):
    # hardcode the quantiles
    qs = np.linspace(0.1, 1, 100, 0)
    q_1 = df_1.quantile(qs)
    q_2 = df_2.quantile(qs)

    rangey = [ min([ q_1.min(), q_2.min()]), max([q_1.max(),q_2.max()]) ]
    rangex = [qs.min(), qs.max()]

    #fig = plt.figure(figsize=(15, 12))
    xlabel_text = 'quantile'
    #ylabel_text = 'annual compensation (USD)'
    #title_text = "quantile distribution for nonDS Men and Women's salaries"
    plt.plot(qs, q_1, 'b.')
    plt.plot(qs, q_2, 'r.')
    plt.plot(.5,df_1.mean(),'b+')
    plt.plot(.5,df_2.mean(),'r+')
    plt.plot(rangex, rangey, color='k')
    plt.gca().set(yscale='log')
    plt.title(title_text)
    plt.ylabel(ylabel_text)
    plt.xlabel(xlabel_text)
    #return plt.gca() 

def plot_quantiles2(df_1, df_2,ylabel_text,title_text): #, xlimit, xlabel_text, ylabel_text, ptype):
    # hardcode the quantiles
    qs = np.linspace(0.1, 1, 100, 0)
    q_1 = df_1.quantile(qs)
    q_2 = df_2.quantile(qs)

    rangey = [ min([ q_1.min(), q_2.min()]), max([q_1.max(),q_2.max()]) ]
    rangex = [qs.min(), qs.max()]

    #fig = plt.figure(figsize=(15, 12))
    xlabel_text = 'quantile'
    #ylabel_text = 'annual compensation (USD)'
    #title_text = "quantile distribution for nonDS Men and Women's salaries"
    plt.plot(qs, q_1/q_2, 'g.') 
    #plt.plot(qs, q_2, 'r.')
    plt.plot(.5,df_1.mean()/df_2.mean(),'go')
    #plt.plot(.5,df_2.mean(),'r+')
    plt.plot(rangex, [1,1], color='k')
    plt.gca().set(yscale='log')
    plt.ylim([.5, 3])
    plt.title(title_text)
    plt.ylabel(ylabel_text)
    plt.xlabel(xlabel_text)
    #return plt.gca() 



