# franka_fr3

## Summary
- Overall coverage: `direct`
- Entry type in `references.bib`: `manual`
- Current cite key: `franka_fr3`

## Corrected Metadata Fields
```bibtex
@manual{franka_fr3,
  author = {{Franka Robotics}},
  title = {Datasheet Franka Research 3},
  organization = {Franka Robotics},
  number = {R02212},
  edition = {2.4},
  month = oct,
  year = {2025},
  url = {https://franka.de/hubfs/Datasheet_FrankaResearch3_R02212_2.4.pdf?hsLang=en},
  note = {Product page: https://franka.de/franka-research-3; FCI overview: https://support.franka.de/docs/overview.html; accessed 2026-04-17}
}
```

## Authoritative URLs
- https://franka.de/franka-research-3
- https://support.franka.de/docs/overview.html

## Call Sites Checked
- line 994 — `partial` — Direct support for 855 mm reach; the workspace-scale interpretation remains an author inference.
  Source text: `Research tabletop arm reach & about $0.855$ m & The Franka Research~3 product page lists an $855$ mm reach; this is a realistic scale for anchor-to-workspace geometry in a lab manipulation setup \citep{franka_fr3}.\\`
- line 995 — `direct` — Direct support for position repeatability below ±0.1 mm under ISO 9283 after the text was corrected.
  Source text: `Robot repeatability & $<\pm 0.1$ mm & The official Franka Research~3 datasheet lists position repeatability below $\pm 0.1$ mm under ISO~9283 \citep{franka_fr3}.\\`
- line 996 — `direct` — Direct support for 1 kHz control/measurement access when paired with the phone-rate citations for the comparison.
  Source text: `Robot control rate & about $1$ kHz low-level control & Official FR3 materials describe $1$ kHz control and measurement access through the Franka Control Interface; this is much faster than $60$ Hz phone video and faster than the $200$ Hz Android sensor-rate limit without the high-rate permission \citep{franka_fr3,pixel9a_specs,android_sensors_overview}.\\`

## Public Artifact
- Artifact type: `pdf`
- Local artifact file: [fulltext.pdf](fulltext.pdf)
- Fulltext source URL: https://franka.de/hubfs/Datasheet_FrankaResearch3_R02212_2.4.pdf?hsLang=en
- Landing page URL: https://franka.de/franka-research-3
- Acquisition status: Downloaded `fulltext.pdf` from https://franka.de/hubfs/Datasheet_FrankaResearch3_R02212_2.4.pdf?hsLang=en.

## Unresolved Issues
- Repointed the entry to the official datasheet/product material and corrected the prose from pose repeatability to position repeatability.
