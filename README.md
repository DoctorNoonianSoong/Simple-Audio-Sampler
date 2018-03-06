# Simple-Audio-Sampler
Creates amplitude samples of a quarter sound wave of given frequency
Tested on Python 3.6.0b2

The first argument (mandatory) is the frequency of a single tone/note.
The second argument (optional) is the sampling rate: how many amplitudes per full second would be recorded.
If second argument not given, sampling rate of 44.1 kHz (44,100 Hz) used by default.

Outputs samples in floating point format to "{note frequency} Hz at Sample Rate of {sample frequency}.txt" in the running directory.
