# barrau2017invariant

## Summary
- Overall coverage: `partial`
- Entry type in `references.bib`: `article`
- Current cite key: `barrau2017invariant`

## Corrected Metadata Fields
```bibtex
@article{barrau2017invariant,
  author = {Barrau, Axel and Bonnabel, Silv{\`e}re},
  title = {The Invariant Extended Kalman Filter as a Stable Observer},
  journal = {IEEE Transactions on Automatic Control},
  volume = {62},
  number = {4},
  pages = {1797--1812},
  year = {2017},
  doi = {10.1109/TAC.2016.2594085},
  url = {https://doi.org/10.1109/TAC.2016.2594085}
}
```

## Authoritative URLs
- https://doi.org/10.1109/TAC.2016.2594085
- https://arxiv.org/abs/1410.1465

## Call Sites Checked
- line 241 — `direct` — Supports Lie-group local-error coordinates and manifold correction steps.
  Source text: `This is why Lie groups are not just a change of notation. They specify how a nonlinear state is locally parameterized and how corrections are injected back onto the manifold \citep{sola2018micro,barrau2017invariant}.`
- line 556 — `partial` — Supports IEKF context, but not the full discrete IMU-noise integration claim by itself.
  Source text: `The discrete noise terms above are not independent free parameters; they arise from integrating $n_g,n_a,w_{bg},w_{ba}$ over $[t_k,t_{k+1}]$, and their joint covariance is summarized by $Q_k$. Equation~\eqref{eq:discrete_process_model_final} is therefore a first-order discretization of the IMU-conditioned state transition used in EKF-, IEKF-, or fixed-lag estimators \citep{mourikis2007msckf,forster2017preintegration,barrau2017invariant}.`
- line 819 — `partial` — Supports recursive IEKF filtering on manifolds, but not the full Gaussian-posterior wording by itself.
  Source text: `replacing each by a Gaussian in local coordinates around a nominal state. This yields EKF, IEKF, or related recursive filters \citep{mourikis2007msckf,barrau2017invariant,sarkka2023bayesian}.`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://arxiv.org/pdf/1410.1465v4
- Landing page URL: https://arxiv.org/abs/1410.1465
- Acquisition status: Downloaded `fulltext.pdf` from https://arxiv.org/pdf/1410.1465v4.

## Unresolved Issues
- Kept as a secondary support cite where the prose is now narrowed toward IEKF/manifold filtering.
