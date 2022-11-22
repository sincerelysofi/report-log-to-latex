"""
log_to_latex.py
by Sofia Lee
v0.1

This program reads a timelog.tsv file and returns a LaTeX table.

If you use this, please credit me! See CITATION.cff in the github.
"""

from datetime import datetime
import pandas as pd
import warnings

# suppress various warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None
pd.set_option('display.max_colwidth', None)

def process_time(time):
    """
    Takes a time and converts it to a datetime object.

    Args:
        time (str): A string consisting of a time expressed as Hour:Minutes.

    Returns:
        a datetime object from the given time
    """
    return datetime.strptime(time, '%H:%M')

def format_time(delta):
    """
    Takes an integer of seconds and converts it to {Hour}h{Minute}m format.

    Args:
        delta (int): A number of seconds.

    returns:
        str: A formatted time difference.
    """
    # convert seconds to minutes
    minutes = delta / 60

    hours = int(minutes / 60)
    minutes = int(minutes % 60)
    
    # Format the time according to what information we have
    if hours > 0 and minutes > 0:
        return f'{hours}h{minutes}m'
    elif hours > 0:
        return f'{hours}h'
    else:
        return f'{minutes}m'

def get_time(begin, end):
    """
    Takes a beginning and an end time and returns the difference in seconds.

    Args:
        begin (str): Start time
        end (str): End time

    Returns:
        int: The number of seconds' difference between the two times.
    """
    
    # convert them to datetime objects
    begin = process_time(begin)
    end = process_time(end)
    
    # get the difference
    delta = end - begin

    return int(delta.total_seconds())

def main():
    try:
        # load the log file to dataframe
        df = pd.read_csv('timelog.tsv', sep='\t', header=0)

        # create an output dataframe
        out_df = df[['Week','Task']]

        # calculate the time difference
        out_df['Time'] = df.apply(lambda x: get_time(x.Begin, x.End), axis=1)

        # format the difference
        out_df['Time spent'] = out_df['Time'].apply(format_time) 

        # output
        output = out_df.to_latex(columns=['Week', 'Task', 'Time spent'],
            index=False)

        total = format_time(out_df['Time'].sum())
        print('\n\n' + output)

        print('Total:', total)

    except FileNotFoundError:
        # the file wasn't found
        print('Error! timelog.tsv missing in working directory. Please make sure this file exists. Exiting...')


if __name__ == '__main__':
    main()
