# Profile assets

- `profile-banner.svg`: original static vector artwork for this profile. The map
  and sensing graphic is a schematic, not experimental data.
- `geoff-sim.gif`: resized recorded G1 pedestrian-plaza simulation from Geoff-Sim.
- `dougie-sim.gif`: resized recorded torque-driven Go2 walking simulation from
  Dougie-Sim. This is a walking preview, not a radiation-mapping mission recording.

Both animations preserve playback duration and fit within a 560 × 350 canvas.
Longer clips are frame-sampled to keep previews compact (at most 48 frames).
They are hosted here so that profile images render without access to the source
repositories. They illustrate separate simulation runs, not measured navigation
performance or hardware deployment. Original project media and upstream notices
remain governed by their respective terms; no blanket asset licence is added.

`sources.json` records the exact source commits and Git blob identifiers.
Regenerate with Pillow and an authenticated GitHub CLI:

```bash
python3 scripts/prepare_media.py
```

Profile research references were checked against the Liverpool thesis record
(DOI `10.17638/03199094`) and Crossref publication metadata in October 2026.
