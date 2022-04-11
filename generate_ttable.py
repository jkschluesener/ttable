#%% imports
import numpy as np
from scipy.stats import t
import pandas as pd

# %% settings
dof = np.arange(5, 16, 1) # degrees of freedom
alpha = np.array([5., 2.5, 1., 0.5, 0.25, 0.1, 0.05]) # in percent
precision = 4 # floating point precision

# %% find the t-score for every combination of dof and percentile from the inverse cumulative distribution
tscores = np.empty((dof.shape[0],alpha.shape[0]))
for idof in range(dof.shape[0]):
    for ia in range(alpha.shape[0]):
        percentile = 1 - (alpha[ia] / 100)
        tscores[idof, ia] = t.ppf(percentile, dof[idof])

# %% convert the array to a pandas dataframe, round precision
df = pd.DataFrame(data=tscores, index=dof, columns=alpha)
df = df.round(precision)

# %% convert to a well-formatted markdown table
table = df.to_markdown()

# %% save the table as a .md plaintext file
with open('ttable.md', 'w') as f:
    f.write(table)
