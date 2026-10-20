import numpy as np 
import plotly.express as px

def plot_signal(signal, fs):
    t = np.arange(len(signal)) / fs

    px.line(x = t, y = signal).show()
