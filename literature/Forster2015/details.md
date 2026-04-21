# Forster2015

## Summary
- Overall coverage: `partial`
- Entry type in `references.bib`: `inproceedings`
- Current cite key: `Forster2015`

## Corrected Metadata Fields
```bibtex
@inproceedings{Forster2015,
  author = {Forster, Christian and Carlone, Luca and Dellaert, Frank and Scaramuzza, Davide},
  title = {IMU Preintegration on Manifold for Efficient Visual-Inertial Maximum-a-Posteriori Estimation},
  booktitle = {Proceedings of Robotics: Science and Systems},
  address = {Rome, Italy},
  month = jul,
  year = {2015},
  doi = {10.15607/RSS.2015.XI.006},
  url = {https://www.roboticsproceedings.org/rss11/p06.html}
}
```

## Authoritative URLs
- https://doi.org/10.15607/RSS.2015.XI.006
- https://www.roboticsproceedings.org/rss11/p06.html

## Call Sites Checked
- line 1305 — `partial` — Supports optimization-based IMU-preintegrated MAP smoothing, but not explicit landmark-state optimization in the way the old wording implied.
  Source text: `The Bayesian inverse-problem perspective treats trajectory and map as latent variables inferred from sensor data and priors \citep{stuart2010inverse}. Recursive Bayesian filtering and smoothing provide the general algorithmic backbone \citep{sarkka2023bayesian}. In visual--inertial robotics, filtering families such as MSCKF keep a Gaussian posterior over the current state and selected pose history \citep{mourikis2007msckf}. Optimization families such as IMU-preintegrated MAP smoothing, OKVIS, and VINS-Mono instead solve nonlinear MAP problems over keyframes or sliding windows of recent states, sometimes with structureless visual factors rather than explicit landmark states \citep{Forster2015,forster2017preintegration,leutenegger2015okvis,VINSMono2017}. Fiducial-tag systems such as TagSLAM explicitly represent static tag poses and body poses together in a factor graph \citep{TagSLAM2019}. Continuous-time Bayesian approaches such as STEAM place priors directly on the space of trajectories and then condition on observations \citep{Barfoot2014,anderson2015gp}. The anchored multi-tag method developed in this report fits naturally in this landscape as either a joint fiducial visual--inertial SLAM estimator or a conservative two-stage approximation to it.`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://www.roboticsproceedings.org/rss11/p06.pdf
- Landing page URL: https://www.roboticsproceedings.org/rss11/p06.html
- Acquisition status: Downloaded `fulltext.pdf` from https://www.roboticsproceedings.org/rss11/p06.pdf.

## Unresolved Issues
- The surrounding prose was softened so the citation now carries only the optimization / MAP / preintegration part it actually supports.
