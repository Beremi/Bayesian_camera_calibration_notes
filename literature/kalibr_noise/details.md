# kalibr_noise

## Summary
- Overall coverage: `direct`
- Entry type in `references.bib`: `misc`
- Current cite key: `kalibr_noise`

## Corrected Metadata Fields
```bibtex
@misc{kalibr_noise,
  author = {{ETH Zurich Autonomous Systems Lab (ASL)}},
  title = {IMU Noise Model},
  year = {2023},
  howpublished = {GitHub wiki},
  url = {https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model},
  note = {Accessed 2026-04-17}
}
```

## Authoritative URLs
- https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model

## Call Sites Checked
- line 424 — `direct` — Now directly supports the bias-random-walk nuisance-model sentence.
  Source text: `The rationale for the prior components is physical. Over short video intervals, position and orientation do not jump discontinuously, so a constant-velocity / constant-angular-velocity prior is a sensible default. The white-noise drives in \eqref{eq:curve_prior_sde_new} provide a simple smoothness model that still admits real maneuvers. Bias random walks are used because MEMS bias drift is slow, cumulative, and not known a priori; a random walk is a common tractable model for a slowly varying nuisance offset and integrates well with filters and smoothers. The same bias-random-walk nuisance model is used in Kalibr and in standard visual--inertial formulations such as MSCKF-style filters and preintegrated optimization methods \citep{kalibr_noise,mourikis2007msckf,forster2017preintegration}.`
- line 966 — `direct` — Direct support for Allan-variance-style estimation of continuous-time white-noise and bias-random-walk parameters.
  Source text: `\item Estimate $R_g,R_a$ and their continuous-time equivalents from stationary IMU data, preferably through Allan deviation analysis. Kalibr's IMU model uses continuous-time white-noise and bias-random-walk parameters of exactly this form \citep{kalibr_noise}.\`
- line 999 — `partial` — Supports units and interpretation for the YAML example values, but not the example values themselves.
  Source text: `Example Kalibr \texttt{imu.yaml} values & $\sigma_a=1.86\times10^{-3}$ m/s$^2/\sqrt{\mathrm{Hz}}$, $\sigma_{ba}=4.33\times10^{-4}$ m/s$^3/\sqrt{\mathrm{Hz}}$, $\sigma_g=1.87\times10^{-4}$ rad/s$/\sqrt{\mathrm{Hz}}$, $\sigma_{bg}=2.66\times10^{-5}$ rad/s$^2/\sqrt{\mathrm{Hz}}$ & Kalibr's YAML-formats page shows these as example \texttt{imu.yaml} entries at an update rate of $200$ Hz; the units and continuous-time interpretation are documented separately in the Kalibr IMU-noise page, so these values are useful as a format-and-units example, not as a phone-specific default \citep{kalibr_yaml_example,kalibr_noise}.\\`

## Public Artifact
- Artifact type: `link`
- Fulltext source URL: https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model
- Landing page URL: https://github.com/ethz-asl/kalibr/wiki/IMU-Noise-Model
- Acquisition status: Removed the saved `fulltext.html` snapshot to avoid storing embedded web-page state in the repository; the authoritative source links are recorded directly in this file.

## Unresolved Issues
- Retitled the entry to the official wiki page title.
