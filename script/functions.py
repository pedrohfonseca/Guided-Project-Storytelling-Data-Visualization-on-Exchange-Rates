import logging
import pandas as pd

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

"""
Test file to be used to pytest
"""

def read_data(file_path):
    """
    Return the dataframe from a csv
    Args:
        file_path (str): Path of file than we will read.
    Return:
        df (pandas dataframe): Dataframe with the data of file.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info("SUCCESS: There are {} rows in your dataframe".format(df.shape[0]))
        return df
    except:
        logging.error("ERROR: we were not able to find {}".format(file_path))

def calculate_rolling_mean(val, window):
    """
    Return the rolling mean calculated
    Args:
        val (pandas Series): Serie with the data than we will apply the rolling mean.
        window (int): Number of samples than we will use.
    Return:
        rolling_mean (pandas Series): Serie with the rolling mean.
    """
    try:
      assert(isinstance(window, int))
      rolling_mean = val.rolling(window).mean()
      logging.info("SUCCESS: The window value is INT".format(window))
      return rolling_mean
    except:
      logging.error("ERROR: Window is not a INT")

def to_datetime(time):
    """
    Return in datetime format
    Args:
        time (pandas Series): Serie with string dtype
    Return:
        date (pandas Series): Serie with datetime dtype
    """
    try:
      date = pd.to_datetime(time)
      logging.info("SUCCESS: Parsing was done")
      return date
    except:
      logging.error("Invalid parsing value")
      