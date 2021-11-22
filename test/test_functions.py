
import pandas as pd
from functions import read_data
from functions import calculate_rolling_mean
from functions import to_datetime

file_path_1 = 'https://github.com/pedrohfonseca/Guided-Project-Storytelling-Data-Visualization-on-Exchange-Rates/blob/main/databases/euro-daily-hist_1999_2021.csv?raw=true'
file_path_2 = 'https://github.com/pedrohfonseca/Guided-Project-Storytelling-Data-Visualization-on-Exchange-Rates/blob/main/databases/USD_BRL%20Dados%20Hist%C3%B3ricos.csv?raw=true'
file_path_3 = 'https://github.com/pedrohfonseca/Guided-Project-Storytelling-Data-Visualization-on-Exchange-Rates/blob/main/databases/USD_BRL%20Dados%20Hist%C3%B3ricos_2.csv?raw=true'

def test_read_data_1():
    assert(isinstance(read_data(file_path_1), pd.DataFrame))

def test_read_data_2():
    assert(isinstance(read_data(file_path_2), pd.DataFrame))

def test_read_data_3():
    assert(isinstance(read_data(file_path_3), pd.DataFrame))

def test_rolling_mean():
    assert(isinstance(calculate_rolling_mean(read_data('dados_resumo.csv')['US_dollar'], 2), pd.Series))

def test_to_datetime():
    assert(isinstance(to_datetime(read_data('dados_resumo.csv')['Time'][0]), pd.Timestamp))