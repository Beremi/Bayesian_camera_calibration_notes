# sola2018micro

## Summary
- Overall coverage: `direct`
- Entry type in `references.bib`: `misc`
- Current cite key: `sola2018micro`

## Corrected Metadata Fields
```bibtex
@misc{sola2018micro,
  author = {Sol{\`a}, Joan and Deray, Jeremie and Atchuthan, Dinesh},
  title = {A micro {Lie} theory for state estimation in robotics},
  year = {2018},
  publisher = {arXiv},
  doi = {10.48550/arXiv.1812.01537},
  eprint = {1812.01537},
  archivePrefix = {arXiv},
  primaryClass = {cs.RO},
  url = {https://arxiv.org/abs/1812.01537}
}
```

## Authoritative URLs
- https://doi.org/10.48550/arXiv.1812.01537
- https://arxiv.org/abs/1812.01537

## Call Sites Checked
- line 241 — `direct` — Supports local tangent-space uncertainty and manifold correction injection.
  Source text: `This is why Lie groups are not just a change of notation. They specify how a nonlinear state is locally parameterized and how corrections are injected back onto the manifold \citep{sola2018micro,barrau2017invariant}.`
- line 267 — `partial` — Supports quaternion-as-manifold and 3D tangent-space uncertainty; the multiplicative-quaternion naming is more direct in sola2017quaternion.
  Source text: `Thus the quaternion representation is \emph{parallel} to the Lie-group representation, not a competing model. One stores orientation by a unit quaternion for convenience, but the Bayesian linearization, covariance, and Kalman update are still performed in a 3D local tangent coordinate. This is the standard ``multiplicative quaternion'' or ``error-state quaternion'' viewpoint \citep{sola2017quaternion,sola2018micro}.`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://arxiv.org/pdf/1812.01537.pdf
- Landing page URL: https://arxiv.org/abs/1812.01537
- Acquisition status: Downloaded `fulltext.pdf` from https://arxiv.org/pdf/1812.01537.pdf.

## Unresolved Issues
- Corrected a miscitation: the repo previously pointed this key at the wrong DOI and venue.
