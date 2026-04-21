# Barfoot2014

## Summary
- Overall coverage: `direct`
- Entry type in `references.bib`: `inproceedings`
- Current cite key: `Barfoot2014`

## Corrected Metadata Fields
```bibtex
@inproceedings{Barfoot2014,
  author = {Barfoot, Tim and Tong, Chi Hay and S{\"a}rkk{\"a}, Simo},
  title = {Batch Continuous-Time Trajectory Estimation as Exactly Sparse Gaussian Process Regression},
  booktitle = {Proceedings of Robotics: Science and Systems},
  volume = {10},
  address = {Berkeley, USA},
  month = jul,
  year = {2014},
  doi = {10.15607/RSS.2014.X.001},
  isbn = {9780992374709},
  url = {https://www.roboticsproceedings.org/rss10/p01.html}
}
```

## Authoritative URLs
- https://doi.org/10.15607/RSS.2014.X.001
- https://www.roboticsproceedings.org/rss10/p01.html

## Call Sites Checked
- line 1305 — `direct` — Direct support for continuous-time GP priors conditioned on observations in the STEAM/RSS formulation.
  Source text: `The Bayesian inverse-problem perspective treats trajectory and map as latent variables inferred from sensor data and priors \citep{stuart2010inverse}. Recursive Bayesian filtering and smoothing provide the general algorithmic backbone \citep{sarkka2023bayesian}. In visual--inertial robotics, filtering families such as MSCKF keep a Gaussian posterior over the current state and selected pose history \citep{mourikis2007msckf}. Optimization families such as IMU-preintegrated MAP smoothing, OKVIS, and VINS-Mono instead solve nonlinear MAP problems over keyframes or sliding windows of recent states, sometimes with structureless visual factors rather than explicit landmark states \citep{Forster2015,forster2017preintegration,leutenegger2015okvis,VINSMono2017}. Fiducial-tag systems such as TagSLAM explicitly represent static tag poses and body poses together in a factor graph \citep{TagSLAM2019}. Continuous-time Bayesian approaches such as STEAM place priors directly on the space of trajectories and then condition on observations \citep{Barfoot2014,anderson2015gp}. The anchored multi-tag method developed in this report fits naturally in this landscape as either a joint fiducial visual--inertial SLAM estimator or a conservative two-stage approximation to it.`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://www.roboticsproceedings.org/rss10/p01.pdf
- Landing page URL: https://www.roboticsproceedings.org/rss10/p01.html
- Acquisition status: Downloaded `fulltext.pdf` from https://www.roboticsproceedings.org/rss10/p01.pdf.

## Unresolved Issues
- Corrected the author field from Charles H. Tong to Chi Hay Tong and added DOI / proceedings metadata.
