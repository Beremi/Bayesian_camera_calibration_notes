# TagSLAM2019

## Summary
- Overall coverage: `partial`
- Entry type in `references.bib`: `article`
- Current cite key: `TagSLAM2019`

## Corrected Metadata Fields
```bibtex
@article{TagSLAM2019,
  author = {Pfrommer, Bernd and Daniilidis, Kostas},
  title = {TagSLAM: Robust SLAM with Fiducial Markers},
  journal = {arXiv preprint arXiv:1910.00679},
  year = {2019},
  doi = {10.48550/arXiv.1910.00679},
  eprint = {1910.00679},
  archivePrefix = {arXiv},
  primaryClass = {cs.RO},
  url = {https://arxiv.org/abs/1910.00679}
}
```

## Authoritative URLs
- https://doi.org/10.48550/arXiv.1910.00679
- https://arxiv.org/abs/1910.00679

## Call Sites Checked
- line 1082 — `partial` — Supports the incremental factor-graph branch of the real-time implementation sentence, but not EKF/fixed-lag wording by itself.
  Source text: `The price is computation and implementation complexity. A real-time version is usually built as a fixed-lag smoother, an EKF-SLAM style filter, or an incremental factor-graph system with a bounded set of actively tracked tags \citep{mourikis2007msckf,leutenegger2015okvis,forster2017preintegration,TagSLAM2019}.`
- line 1299 — `direct` — Now supports the generic factor-graph-systems comparison after the prose was narrowed.
  Source text: `Yes. The staggered scheme is a reasonable option provided it is described honestly. It is not the exact joint posterior described in Chapter~1, but it is a principled approximation of it. In many practical systems this is a practical trade-off: the front-end manages raw pixels and geometry, the back-end manages real-time propagation and correction, and a slower map-refinement layer repairs the parts of the posterior that the fast filter cannot represent exactly. This is close in spirit to many mature recursive, smoothing, and factor-graph estimation systems even when they are not written in exactly the same notation \citep{mourikis2007msckf,leutenegger2015okvis,forster2017preintegration,kaess2012isam2,TagSLAM2019}.`
- line 1305 — `direct` — Direct support for joint body-pose and static-tag factor-graph modeling.
  Source text: `The Bayesian inverse-problem perspective treats trajectory and map as latent variables inferred from sensor data and priors \citep{stuart2010inverse}. Recursive Bayesian filtering and smoothing provide the general algorithmic backbone \citep{sarkka2023bayesian}. In visual--inertial robotics, filtering families such as MSCKF keep a Gaussian posterior over the current state and selected pose history \citep{mourikis2007msckf}. Optimization families such as IMU-preintegrated MAP smoothing, OKVIS, and VINS-Mono instead solve nonlinear MAP problems over keyframes or sliding windows of recent states, sometimes with structureless visual factors rather than explicit landmark states \citep{Forster2015,forster2017preintegration,leutenegger2015okvis,VINSMono2017}. Fiducial-tag systems such as TagSLAM explicitly represent static tag poses and body poses together in a factor graph \citep{TagSLAM2019}. Continuous-time Bayesian approaches such as STEAM place priors directly on the space of trajectories and then condition on observations \citep{Barfoot2014,anderson2015gp}. The anchored multi-tag method developed in this report fits naturally in this landscape as either a joint fiducial visual--inertial SLAM estimator or a conservative two-stage approximation to it.`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://arxiv.org/pdf/1910.00679
- Landing page URL: https://arxiv.org/abs/1910.00679
- Acquisition status: Downloaded `fulltext.pdf` from https://arxiv.org/pdf/1910.00679.

## Unresolved Issues
- Augmented the entry with DOI/eprint metadata for the arXiv record.
