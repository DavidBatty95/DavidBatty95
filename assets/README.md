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
