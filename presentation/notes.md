# Structured Multilinear Dsicriminant Analysis for ERP classification

* What is the message? Performance can be improved with structured covariance
  estimation
* Know which slide comes next
* Transition between slides

## Who am i

## Need/Task
Working on covert attention visual BCIs
for patients with eye movement problems

need for better ERP decoding algorithms

### Spatiotemporal analysis
ERPs are spatiotemporal, they contain features distributed in space (channels) and time
(samples)

Especially for covert attention, all information we can get is needed

### Curse of dimensionality for linear classifiers
A linear like LDA needs to estimate the covariance and inverse covariance of
ERP data

For full spatiotemporal EEG this leads to giant cov matrix
especially for high-density/high-resolution data

* slow, high memory usage
* a lot of training data needed
* prone to overfitting

### Usual solutions
dimensionality reduction
* feature selection (e.g. sLDA, channel selection)
* feature projection to single domain (e.g. CSP, spatial beamforming, Riemannian
  Geometry)

### Alternative solution
What if we want to use all spatiotemporal information present

Find a way to reduce number of intermediary parameters

## Main points
#### Orthogonal decomposition of cov
On first sight, the covariance does not look random, but structured

REsearch has shown that it follows the model of superposition of stationary noise sources since noise is non-time locked

decomposition in Kronecker-Toeplitz sum

First component contains most noise, is often sufficient

Calculate inverse, nice mathematical properties,
can be combined with usual shrinkage regularization

#### Time and memory improvements

Less parameters to keep in memory

Calculation is much faster

scalable

#### Accuracy improvements regularization
LDA competitive
Shorten required calibration length

## Review
Stationary spatiotemporal noise sources model leads to structured covariance

## Conclusion
Simple assumption of single kronecker-toeplitz term leads to
* Faster training
* Less memory
* Better performance for low data availability hence shorter calibration time
