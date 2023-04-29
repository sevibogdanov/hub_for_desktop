import pandas as pd
import datetime
import matplotlib.pyplot as plt


def target_weight():
    df = pd.read_csv('weight.txt', sep='\t')
    return float(df[df['service']=='target']['weight'].values)
def min_weight():
    df = pd.read_csv('weight.txt', sep='\t')
    return float(df[df['service'].isna()]['weight'].min())

def max_weight():
    df = pd.read_csv('weight.txt', sep='\t')
    return float(df[df['service'].isna()]['weight'].max())

def current_weight():
    df = pd.read_csv('weight.txt', sep='\t')
    return float(df[df['service'].isna()]['weight'].iloc[len(df)-2])

def read_file():
    df = pd.read_csv('weight.txt',sep='\t')
    return df

def write_file(current_weight):
    df = pd.read_csv('weight.txt', sep='\t')
    df.loc[len(df)] = [float(current_weight),datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),None]
    df.to_csv('weight.txt',sep='\t',index=False)

def table_text():
    df = pd.read_csv('weight.txt', sep='\t',parse_dates=[1])
    df= df[df['service'].isna()]
    df = df[['weight','time']] #.sort_values('time',ascending=False)
    df = df.reset_index()[['weight','time']]
    text = ''

    print(df)

    if len(df) > 20:
        x = 20
    else:
        x = len(df)
    for each in range(x):
        each = len(df)-each-1
        text += str(df.iloc[each,0])
        if each < len(df)-1:
            if df.iloc[each,0] < df.iloc[each+1,0]:
                text += '    ▼    '
            elif df.iloc[each,0] == df.iloc[each+1,0]:
                text += '    ▬    '
            else:
                text += '    ▲    '
        else:
            text += '    ▬    '
        text += str(df.iloc[each,1].strftime('%H:%M   %d.%m.%y')) + '\n'
    return text

def make_graph():
    df = pd.read_csv('weight.txt', sep='\t', parse_dates=[1])
    df = df[df['service'].isna()]
    df = df[['weight', 'time']].sort_values('time')
    df['sort'] = df['time']
    df['time'] = df['time'].dt.strftime('%d.%m.%y')
    df = df.groupby('time').max()
    df['timee'] = df.index
    df['timee'] = df['timee'].astype('datetime64[ns]')
    df.reset_index(inplace=True)
    df = df.sort_values('timee')
    df = df.tail(12)
    df['timee'] = df['timee'].dt.strftime('%d.%m.%y')

    plt.plot(df['timee'], df['weight'], linewidth=3,marker = 'o',color='orange')
    plt.grid(False)
    plt.axis('off')
    for x,y in zip(df['timee'],df['weight']):
        label = "{:.1f}".format(y)
        plt.annotate(label, # this is the text
                     (x,y), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center',
                     color='white') # horizontal alignme
        # label = x
        # plt.annotate(label,  # this is the text
        #              (x, y),  # these are the coordinates to position the label
        #              textcoords="offset points",  # how to position the text
        #              xytext=(0, -15),  # distance from text to points (x,y)
        #              ha='center',
        #              color='grey',
        #              rotation=0,
        #              fontsize=7)  # horizontal alignme

        df = pd.read_csv('weight.txt', sep='\t', parse_dates=[1])
        df = df[df['service'].isna()]
        df = df[['weight', 'time']].sort_values('time')
        df['sort'] = df['time']
        df['time'] = df['time'].dt.strftime('%d.%m.%y')
        df = df.groupby('time').min()
        df['timee'] = df.index
        df['timee'] = df['timee'].astype('datetime64[ns]')
        df.reset_index(inplace=True)
        df = df.sort_values('timee')
        df = df.tail(12)
        df['timee'] = df['timee'].dt.strftime('%d.%m.%y')

        plt.plot(df['timee'], df['weight'], linewidth=3, marker='o',color='blue')
        plt.grid(False)
        plt.axis('off')
        for x, y in zip(df['timee'], df['weight']):
            label = "{:.1f}".format(y)
            plt.annotate(label,  # this is the text
                         (x, y),  # these are the coordinates to position the label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center',
                         color='white',
                         size=10)  # horizontal alignme
            label = x
            plt.annotate(label,  # this is the text
                         (x, y),  # these are the coordinates to position the label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, -15),  # distance from text to points (x,y)
                         ha='center',
                         color='grey',
                         rotation=0,
                         fontsize=7)  # horizontal alignme

    plt.savefig('graph.png',transparent=True,figsize=(10, 10))
    plt.close()

def target_weight_change(x):
    df = pd.read_csv('weight.txt', sep='\t')
    df.iloc[0, 0] = float(x)
    df.to_csv('weight.txt', sep='\t', index=False)
