import IPython
import sklearn as sk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print 'IPython version:', IPython.__version__
print 'numpy version:', np.__version__
print 'scikit-learn version:', sk.__version__
print 'matplotlib version:', matplotlib.__version__

from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')