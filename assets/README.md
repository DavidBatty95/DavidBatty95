# Profile assets

- `profile-banner.svg`: prominent vector introduction with David's role,
  qualifications, four project areas and a skills strip identifying ROS 1 Noetic
  and ROS 2 Humble. The map and sensing motif is a schematic, not experimental data.
- `nav-*.svg`: locally hosted section-navigation buttons with accessible labels.
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

## Project showcases

The Current Research section was refreshed on 14 October 2026:

- `geoff-showcase.svg`: original G1 locomanipulation illustration, with observed
  pickup, a carried cube, target pad and the observe/dock/carry/verify pipeline.
- `dougie-showcase.svg`: original Go2 illustration in a multi-level facility,
  with a radiation source, sensing arcs, service ramps and a return route.
- Both cards use a coordinated midnight palette, project-specific cyan/amber
  accents, large titles, accessible SVG descriptions, subtle route/pulse motion
  and reduced-motion support. They are schematics, not live telemetry.
- `geoff-locomanipulation.gif`: resized actual MuJoCo pickup/lift excerpt from
  Geoff run `20261014T164500Z-readme-settling`. The source run later fell during
  delivery navigation. Original frame durations and the outcome end card are
  retained. No complete-delivery or physical finger-grasp claim is implied.
- `dougie-multilevel.gif`: newly rendered accelerated replay of actual seed-3
  detector positions from the full-height facility dataset. It shows XYZ motion
  and height history; the floor outlines are reference planes, not a reconstructed
  map. It is not video, a learned radiation field or complete-coverage evidence.
  The final dose is labelled as the recorded outcome, not a live cumulative trace.

Nonanimated alternatives: [Geoff](geoff-locomanipulation.png) and
[Dougie](dougie-multilevel.png). The earlier `geoff-sim.gif` and `dougie-sim.gif`
remain historical assets, with their original identities in `sources.json`.

`project-showcase-sources.json` records source repository revisions, source-file
hashes and dirty state, the selected Dougie outcome and source measurement hashes,
and all generated asset SHA-256 hashes. To regenerate using local checkouts and
Pillow (DejaVu Sans is used for raster labels):

```bash
python3 scripts/build_project_showcase.py --geoff /path/to/Geoff-Sim --dougie /path/to/Dougie-Sim
python3 scripts/check_profile.py
```

## Geoff-Sim-VR showcase

`geoff-vr-showcase.svg` is original schematic artwork added for the
[Geoff-Sim-VR](https://github.com/DavidBatty95/Geoff-Sim-VR) profile tile. It matches
the Geoff/Dougie card dimensions and midnight palette, with violet accents,
accessible SVG descriptions and reduced-motion support. The headset, controllers
and robot arms illustrate the tracking/control/stereo pipeline; they are not
recorded headset footage or evidence of physical robot operation. Project scope
was checked against repository revision `9069b1f84d42fd4492ac3971d9ba5a7d85e4d70a`.
The SVG is maintained directly; the earlier two-card generator does not generate it.

## Tile-led profile directory

The profile now separates Current Research (Skele-Tracker), Virtual Engineering
Centre Projects (Geoff-Sim and Geoff-Sim-VR), and PhD Research Code. The three
research-code cards link independently to the Python abstraction repository,
the ROS 1 repository and Dougie-Sim for ROS 2.

- `skele-tracker-showcase.svg`: original movement/model schematic, informed by
  Skele-Tracker revision `c6ce204f8fcb23f6f84b9641d1e1000174d0ff00`. It contains no
  participant data or clinical-validity claim.
- `research-python.svg`, `research-ros1.svg`, `research-dougie-ros2.svg`: original
  compact research-code cards, with separate repository destinations.
- `pepper-showcase.svg`: original conversational-robot illustration.
- `nav-vec-projects.svg`: navigation to the Virtual Engineering Centre section.

These SVGs are maintained directly. The older experiment GIFs and their source
manifests remain available here; their detailed captions now live with the
project documentation rather than the tile-led profile.

## EmotiBit postdoctoral research card

`sony-emotibit-research.svg` is original schematic artwork for the profile.
Its illustrative waveforms are not experimental results. No participant records,
demographics or physiological traces were copied from the private research repo.
The description of postdoctoral work for Sony Europe and Japan and continuing
use by Tom Gallagher in Professor Alan Marshall's research group was supplied
by David Batty for this profile update in October 2026.

## Aardvark website screenshots

- `aardvark-desktop.png`: real 1440 × 1000 desktop viewport capture.
- `aardvark-mobile.png`: real 390 × 844 mobile-emulated viewport capture.
- Source: <https://aardvarkesuwebsite.onrender.com/>, the public homepage of
  Aardvark Explorer Scout Unit in South Liverpool.
- Captured on 7 October 2026 using Chromium, at device scale factor 1, after
  fonts and visible images loaded. Reduced motion was requested and screenshot
  animations disabled to make a stable still. Site content was not replaced.
- The screenshots show the public development site. No login, member portal,
  forms or private records were accessed. They demonstrate the website's visible
  presentation, not an accessibility audit or backend/security assessment.
- Site imagery and Scouts branding retain their existing rights; the screenshots
  document David's web-development work and do not introduce a new asset licence.

`aardvark-capture.json` records source URL, page title, UTC timestamp, viewport,
browser version, SHA-256 hashes and file sizes. To refresh with Python 3.10+:

```bash
python -m pip install playwright==1.58.0
python -m playwright install chromium
python scripts/capture_aardvark.py
```

On a minimal Linux host, Playwright may also require its documented browser
system dependencies. Capturing again will reflect the site's current state;
update the date in the profile caption when replacing the images.
