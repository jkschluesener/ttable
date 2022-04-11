# ttable

generate t-distribution tables / student's t-tables

This short python script generates tables of critical tscores for combinations of degrees of freedom and alpha thresholds.  
Yes, just like these large tables in classical statistics textbooks!  
You won't realize you need them until you do. :space_invader:

Otherwise, it could just be nice to review this, perhaps maybe, or maybe perhaps not.

## How to use this script

You need to adapt the following variables to your needs:

- `dof`: degrees of freedom usually used in your area of study
- `alpha`: alpha threshold levels interesting to you - in percent, so an alpha of 0.05 is 5%
- `precision`: Number of decimal places

## Dependencies

Virtually any modern-ish python with `numpy`, `scipy` and `pandas`.

## Alpha (and percentiles)

This code uses alpha as a threshold of significance, as is the norm.
If you wish to use percentiles of the normal distribution rather than alpha, just replace the table header with `percentile = 1-alpha`.

## Number of tails

The tables are generated for one-tailed t-tests, for two-tailed t-tests, request an appropriate alpha.

## How this works

The inverse cumulative distribution value returns the t-score for a probability.  
(Think: "returns the x-value of where is the percentile 1-alpha is reached").

Code snippet:

```python
from scipy.stats import t

alpha      = 5 # in percent
dof        = 8 # degrees of freedom
percentile = 1 - (alpha / 100)

tscore = t.ppf(percentile, dof)

print(tscore) # 1.8595480375228424
```

You can check the result using the cumulative density function, which is the reverse (of the inverse :dart:).  
(Think: "returns 1-alpha for a x-value").

Code snippet:

```python
from scipy.stats import t

dof        = 8 # degrees of freedom
tscore     = 1.8595480375228424 # previously computed

percentile = t.cdf(tscore, dof)

alpha      = (1-percentile)*100 # in percent

print(percentile) # 0.9499999999993815
print(alpha) # 5.0000000000618545
```