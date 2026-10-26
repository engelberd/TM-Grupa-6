import numpy as np 
import plotly.express as px

def plot_signal(signal, fs, title="Waveform"):
    t = np.arange(len(signal)) / fs

    fig = px.line(x = t, y = signal)
    fig.update_layout(
        title=title,
        xaxis_titel="Time [s]",
        yaxis_title="Amplitude",

        template="plotly_dark"
    )
    fig.show()


def plot_stft(t, f, S, scale="log", title="STFT"):
    magnitude = np.abs(S)
    
    if scale == "log":
        Z = 20*np.log10(np.maximum(magnitude, 2**-15))
    elif scale == "linear":
        Z = magnitude
    else:
        raise ValueError("scale options: 'log' or 'linear' ")

    fig = px.imshow(
        Z, x=t, y=f,
        origin="lower",
        aspect="auto",
        labels={
            "x": "Time[s]",
            "y": "Frequency [Hz]",
            "color": "Magnitude [dB]" if scale == "log" else "Magnitude"
        },
        title = f"{title} ({scale})"
    )

    fig.update_layout(template="plotly_dark")

    fig.show()


from utils.stft import compute_stft

def preview_stft(signal, fs, scale="log"):
    t, f, S = compute_stft(signal, fs)
    plot_stft(t, f, S, scale=scale)
    return t, f, S