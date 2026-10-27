import numpy as np
from scipy.signal import ShortTimeFFT



def compute_stft(
    signal, fs, *, frame_ms=20, overlap=0.5, hop=None,
    window="hann", mfft=None, fft_mode="onesided2X",
    scale_to="magnitude", remove_mean=False,
    padding="zeros", phase_shift=0, axis=-1,
):
    signal = np.asarray(signal)

    if remove_mean == True:
        signal = signal - np.mean(signal, axis=axis)

    if signal.ndim == 0 or signal.size == 0:
        raise ValueError("signal must be a non-empty array")
    if fs <= 0: 
        raise ValueError("fs must be positive")
    if frame_ms <= 0:
        raise ValueError("frame_ms must be positive")

    frame_len = round(fs * frame_ms / 1000)
    if frame_len < 2:
        raise ValueError("frame_ms produces not enought samples")

    if hop is None:
        hop = round(frame_len * (1 - overlap))

    stft = ShortTimeFFT.from_window(
        win_param=window,
        fs=fs,
        nperseg=frame_len,
        noverlap=frame_len - hop,
        fft_mode=fft_mode,
        mfft=mfft,
        scale_to=scale_to,
        phase_shift=phase_shift,
    )

    S = stft.stft(signal, padding=padding, axis=axis)


    return stft.t(signal.shape[axis]), stft.f, S
