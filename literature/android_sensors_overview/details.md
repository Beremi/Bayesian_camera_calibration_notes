# android_sensors_overview

## Summary
- Overall coverage: `direct`
- Entry type in `references.bib`: `misc`
- Current cite key: `android_sensors_overview`

## Corrected Metadata Fields
```bibtex
@misc{android_sensors_overview,
  author = {{Android Developers}},
  title = {Sensors Overview},
  year = {2026},
  howpublished = {Android Developers documentation},
  url = {https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview},
  note = {Accessed 2026-04-17}
}
```

## Authoritative URLs
- https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview

## Call Sites Checked
- line 993 — `direct` — Direct support for the Android 12+/API 31 sensor rate limit without the high-rate permission.
  Source text: `Phone motion-sensor rate & $200$ Hz limit for \texttt{registerListener()} on Android 12+ apps without the high-rate permission & Android documents that, for apps targeting Android~12 (API level~31) or higher, \texttt{registerListener()} is rate-limited to $200$ Hz for the affected motion and position sensors unless the app declares \texttt{HIGH\_SAMPLING\_RATE\_SENSORS} \citep{android_sensors_overview}.\\`
- line 996 — `direct` — Direct support for the 200 Hz comparison used in the FR3 control-rate row.
  Source text: `Robot control rate & about $1$ kHz low-level control & Official FR3 materials describe $1$ kHz control and measurement access through the Franka Control Interface; this is much faster than $60$ Hz phone video and faster than the $200$ Hz Android sensor-rate limit without the high-rate permission \citep{franka_fr3,pixel9a_specs,android_sensors_overview}.\\`

## Public Artifact
- Artifact type: `link`
- Fulltext source URL: https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview
- Landing page URL: https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview
- Acquisition status: Removed the saved `fulltext.html` snapshot to avoid storing embedded web-page state in the repository; the authoritative source links are recorded directly in this file.

## Unresolved Issues
- Normalized the URL to the canonical Android Developers path.
