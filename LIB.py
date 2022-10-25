#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from functools import reduce
import numpy as np
from datetime import datetime

import folium
import selenium #pip install SELENIUM

import streamlit as st #pip install streamlit 
from streamlit_option_menu import option_menu # 

import plotly.express as px #pip install plotly
from PIL import Image

from geopy.geocoders import Nominatim #pip install geopy
import time
from pprint import pprint

import matplotlib.pyplot as plt
import sqlite3
from sqlite3 import connect

import warnings
warnings.filterwarnings("ignore")


from dateutil import relativedelta #pip install python-dateutil