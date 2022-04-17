# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
from splane import analyze_sys, pretty_print_bicuad_omegayq

num = np.array([1,-1]) 
den = np.array([1,1])

pretty_print_bicuad_omegayq(num,den)
tsf = sig.TransferFunction(num,den)

plt.close('all')
analyze_sys(tsf, 'Respuesta del pasatodo')