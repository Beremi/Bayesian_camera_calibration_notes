# VINSMono2017

## Summary
- Overall coverage: `direct`
- Entry type in `references.bib`: `article`
- Current cite key: `VINSMono2017`

## Corrected Metadata Fields
```bibtex
@article{VINSMono2017,
  author = {Qin, Tong and Li, Peiliang and Shen, Shaojie},
  title = {VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator},
  journal = {IEEE Transactions on Robotics},
  volume = {34},
  number = {4},
  pages = {1004--1020},
  year = {2018},
  doi = {10.1109/TRO.2018.2853729},
  url = {https://doi.org/10.1109/TRO.2018.2853729},
  eprint = {1708.03852},
  archivePrefix = {arXiv},
  primaryClass = {cs.RO}
}
```

## Authoritative URLs
- https://doi.org/10.1109/TRO.2018.2853729
- https://arxiv.org/abs/1708.03852

## Call Sites Checked
- line 1305 — `direct` — Direct support for bounded sliding-window nonlinear optimization-based VIO.
  Source text: `The Bayesian inverse-problem perspective treats trajectory and map as latent variables inferred from sensor data and priors \citep{stuart2010inverse}. Recursive Bayesian filtering and smoothing provide the general algorithmic backbone \citep{sarkka2023bayesian}. In visual--inertial robotics, filtering families such as MSCKF keep a Gaussian posterior over the current state and selected pose history \citep{mourikis2007msckf}. Optimization families such as IMU-preintegrated MAP smoothing, OKVIS, and VINS-Mono instead solve nonlinear MAP problems over keyframes or sliding windows of recent states, sometimes with structureless visual factors rather than explicit landmark states \citep{Forster2015,forster2017preintegration,leutenegger2015okvis,VINSMono2017}. Fiducial-tag systems such as TagSLAM explicitly represent static tag poses and body poses together in a factor graph \citep{TagSLAM2019}. Continuous-time Bayesian approaches such as STEAM place priors directly on the space of trajectories and then condition on observations \citep{Barfoot2014,anderson2015gp}. The anchored multi-tag method developed in this report fits naturally in this landscape as either a joint fiducial visual--inertial SLAM estimator or a conservative two-stage approximation to it.`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://arxiv.org/pdf/1708.03852
- Landing page URL: https://arxiv.org/abs/1708.03852
- Acquisition status: Downloaded `fulltext.pdf` from https://arxiv.org/pdf/1708.03852.

## Unresolved Issues
- Added the journal DOI and retained arXiv metadata for public access.
