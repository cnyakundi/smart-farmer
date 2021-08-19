import pandas as pd
import numpy as np


def load_data(data):
    data=pd.read_csv(data)
    return data

def strip(val):
  striped = val.str.strip()
  return striped

#checking for null

def nuls(val):
  no_null = val.isnull().sum()
  return no_null

# Check for duplicates 
def duplicates(val):
  no_duplicate=val.duplicated().sum()
  return no_duplicate

def check_info(val):
  c_info = val.info()
  return c_info

def means(values):
  the_mean = sum(values)/len(values)
  return the_mean
