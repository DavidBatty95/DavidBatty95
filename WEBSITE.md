# David Batty — HTML portfolio

A responsive, static robotics portfolio based on the content and midnight / teal /
ice-blue visual language of the DavidBatty95 profile.

## Preview locally

From this repository:

```sh
python3 -m http.server 8000
```

Open <http://localhost:8000>. You can also open `index.html` directly in a browser.
There is no build step or application server.

## Publish with GitHub Pages

Once the website files are committed and pushed to `main`, open the repository's
**Settings → Pages**. Under **Build and deployment**, choose **Deploy from a
branch**, then **main** and **/ (root)**, and save.

For the existing `DavidBatty95/DavidBatty95` repository, the Pages address is
<https://davidbatty95.github.io/DavidBatty95/>. GitHub shows the final published
address in the Pages settings after deployment.

## Editing

- `index.html`: project descriptions, research, publications and contact links.
- `styles.css`: responsive layouts, colours, typography and reduced-motion styles.
- `site.js`: decorative canvas robot, occupancy grid, A* route planning and controls.
- `assets/robot-mark.svg`: website icon and navigation mark.
- `assets/`: the existing project artwork and engineering CV.

The background robot plans collision-free routes through an illustrative occupancy
grid. Click open space in the hero map to redirect it, or focus the map and press
Enter or Space to choose a new destination. **Pause motion** stops the canvas;
the system reduced-motion preference starts it paused. Browser tabs that are
hidden suspend rendering. The simulation is illustrative, not live telemetry.

The portfolio content and navigation work without JavaScript. Fonts use Google
Fonts with local system fallbacks. All project illustrations and the CV are local.
See `assets/README.md` for existing media provenance.
