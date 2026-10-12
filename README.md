<a id="top"></a>

<div align="center">
  <img src="assets/profile-banner.svg" width="100%" alt="Meet Dr David Batty — robotics researcher and AI &amp; Cyberphysical Systems Engineer. Geoff-Sim and Dougie-Sim, radiation-aware PhD research, EmotiBit Immersion Measurement, Pepper and freelance web development. Toolkit: ROS 1 Noetic, ROS 2 Humble, Python, Docker, Linux, MuJoCo, Gazebo, RViz, SLAM and Gaussian processes.">

  <p><strong>AI &amp; Cyberphysical Systems Engineer · Robotics Researcher · PhD, University of Liverpool</strong></p>
  <p>Virtual Engineering Centre · University of Liverpool · United Kingdom</p>

  <p>
    <a href="#current-research"><img src="assets/nav-current-research.svg" width="205" height="48" alt="Current Research"></a>
    <a href="#phd-research"><img src="assets/nav-phd-research.svg" width="205" height="48" alt="PhD Research"></a>
    <a href="#web-development"><img src="assets/nav-web-development.svg" width="205" height="48" alt="Web Development"></a>
    <a href="#other-projects"><img src="assets/nav-other-projects.svg" width="205" height="48" alt="Other Projects"></a>
  </p>

  <p>
    <a href="https://livrepository.liverpool.ac.uk/3199094/">PhD thesis</a> &nbsp; / &nbsp;
    <a href="#selected-publications">Publications</a> &nbsp; / &nbsp;
    <a href="https://orcid.org/0009-0003-5375-421X">ORCID</a> &nbsp; / &nbsp;
    <a href="https://uk.linkedin.com/in/david-batty">LinkedIn</a> &nbsp; / &nbsp;
    <a href="mailto:dwbatty@liverpool.ac.uk">Contact</a>
  </p>
</div>

## Building robots that understand their environment

I develop robotic systems that connect **perception, planning and physical action**. My work spans radiation-aware exploration in hazardous nuclear environments, humanoid simulation and human-aware navigation, and conversational robotics for public engagement.

My research brings together **compact map representations, probabilistic environmental modelling and risk-aware decision-making**, with a focus on turning algorithms into integrated, inspectable robotic systems.

Alongside robotics, I also do **freelance web development** for local groups and organisations.

---

## Current Research

Ongoing work in robotic autonomy, radiation-aware exploration and human-aware navigation.

### Robotics and autonomous systems

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DavidBatty95/Geoff-Sim">Geoff-Sim</a></h3>
      <p><strong>Humanoid autonomy around people</strong></p>
      <a href="https://github.com/DavidBatty95/Geoff-Sim"><img src="assets/geoff-sim.gif" width="100%" alt="Recorded MuJoCo simulation of the Unitree G1 walking in a pedestrian plaza"></a>
      <p>Unitree G1 research platform combining locomotion, simulated onboard sensing, online mapping and human-aware navigation in reproducible environments.</p>
      <p><code>Unitree G1</code> <code>ROS 2</code> <code>MuJoCo</code></p>
      <p><a href="https://github.com/DavidBatty95/Geoff-Sim">Explore Geoff-Sim →</a></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DavidBatty95/Dougie-Sim">Dougie-Sim</a></h3>
      <p><strong>Quadruped exploration under radiation constraints</strong></p>
      <a href="https://github.com/DavidBatty95/Dougie-Sim"><img src="assets/dougie-sim.gif" width="100%" alt="Recorded torque-driven Unitree Go2 walking simulation in MuJoCo"></a>
      <p>Unitree Go2 simulation connecting physical locomotion, radiation sensing, online Gaussian process mapping and dose-aware exploration with return-budget reasoning.</p>
      <p><code>Unitree Go2</code> <code>Gaussian processes</code> <code>MuJoCo</code></p>
      <p><a href="https://github.com/DavidBatty95/Dougie-Sim">Explore Dougie-Sim →</a></p>
    </td>
  </tr>
</table>

<sub>Recorded simulation previews from separate runs; project documentation contains the evaluation results. Geoff-Sim and Dougie-Sim are currently private repositories: source links require access. <a href="mailto:dwbatty@liverpool.ac.uk">Contact me about the projects.</a></sub>

[↑ Back to top](#top)

---

## PhD Research

> ### Radiation Aware Navigation and Planning for Mobile Robot Exploration of Unknown Hazardous Nuclear Environments
> **David Batty · PhD thesis · University of Liverpool · 2026**
>
> A unified framework for resource-constrained mobile robots to explore unknown nuclear environments while accounting for radiation exposure.
>
> **[Read the thesis at the University of Liverpool →](https://livrepository.liverpool.ac.uk/3199094/)** &nbsp; · &nbsp; [Permanent DOI](https://doi.org/10.17638/03199094)

The thesis connects four research contributions:

- **Occupancy-map abstraction** — transform dense occupancy grids into lightweight node–edge networks for higher-level planning.
- **Radiation-aware navigation** — incorporate hazard-weighted scoring and modified A* planning to balance exposure and travel distance.
- **Online environmental inference** — use Gaussian process regression to estimate radiation fields during exploration.
- **Physical validation** — combine ultrasonic radiation emulation with a ROS 2 implementation on the Unitree Go2 quadruped.

### Research code: from algorithms to hardware

| Repository | Research focus |
| :--- | :--- |
| [Occupancy-map abstraction · Python](https://github.com/DavidBatty95/OccMapAbstraction-Python-Based) | Benchmarking map abstraction for exploration of unknown environments |
| [Radiation-aware framework · ROS 1](https://github.com/DavidBatty95/OccMapAbstractionROS1Pkg) | Simulation testing of the radiation-aware abstraction framework |
| [Go2 experimental workspace · ROS 2](https://github.com/DavidBatty95/Go2OccMapAbstractionROS2ws) | Real-world testing of radiation-aware exploration on the Unitree Go2 |

### Selected publications

**Real-World Testing of Ultrasonic Beacons for Mobile Robot Radiation Emulation**<br>
David Batty, Andrew West, Ipek Caliskanelli and Paolo Paoletti.<br>
*Towards Autonomous Robotic Systems — TAROS 2024*, pp. 302–312. Springer; published online December 2024, volume year 2025.<br>
[Read publication →](https://doi.org/10.1007/978-3-031-72059-8_26)

**Occupancy Map Abstraction for Higher Level Mission Planning of Autonomous Robotic Exploration in Hazardous Nuclear Environments**<br>
David Batty, Lupo Manes, Andrew West, Maulik Patel, Ipek Caliskanelli and Paolo Paoletti.<br>
*Towards Autonomous Robotic Systems — TAROS 2023*, pp. 77–88. Springer, 2023.<br>
[Read publication →](https://doi.org/10.1007/978-3-031-43360-3_7)

[↑ Back to top](#top)

---

## Web Development

I also build **responsive websites for local groups and organisations**, bringing
the same attention to clear interfaces and practical delivery to my freelance
web-development work.

### Aardvark Explorer Scout Unit

A website I am developing for a **local Scout group in South Liverpool**,
bringing its programme, stories, gallery, leader information and joining routes
together in a clear desktop and mobile experience.

<table>
  <tr>
    <td width="76%" valign="top">
      <a href="https://aardvarkesuwebsite.onrender.com/"><img src="assets/aardvark-desktop.png" width="100%" alt="Desktop screenshot of the Aardvark Explorer Scout Unit website, showing the navigation and Adventure starts here homepage"></a>
    </td>
    <td width="24%" valign="top">
      <a href="https://aardvarkesuwebsite.onrender.com/"><img src="assets/aardvark-mobile.png" width="100%" alt="Mobile screenshot of the Aardvark Explorer Scout Unit website with compact navigation and joining links"></a>
    </td>
  </tr>
</table>

<sub>Actual screenshots of the public development site, captured 7 October 2026. Desktop and mobile browser views; the website continues to evolve.</sub>

`Freelance web development` · `Responsive design` · `Community websites` · `Render deployment`

**[Visit the live website →](https://aardvarkesuwebsite.onrender.com/)** &nbsp; · &nbsp;
**[Discuss a website project →](mailto:dwbatty@liverpool.ac.uk)**

[↑ Back to top](#top)

---

## Other Projects

Applied robotics for public engagement and previous research projects.

### [Pepper-Assistant](https://github.com/DavidBatty95/pepper_assistant)

**Conversational robotics for the Virtual Engineering Centre.** A voice-driven assistant for SoftBank Pepper, designed for demonstrations, tours and visitor Q&A. The system connects wake-word activation, voice activity detection, Vosk speech recognition, GPT-powered dialogue and a Pepper-side speech bridge, with a live terminal dashboard.

`Human–robot interaction` · `Python` · `Speech recognition` · `Conversational AI`

**[Explore Pepper-Assistant →](https://github.com/DavidBatty95/pepper_assistant)**

### EmotiBit Immersion Measurement — previous postdoctoral work

[![EmotiBit Immersion Measurement — previous postdoctoral research for Sony Europe and Japan, with schematic signal traces](assets/sony-emotibit-research.svg)](https://github.com/DavidBatty95/SonyEmotiBitAnalysis)

I developed this work during my **PostDoc for Sony Europe and Japan**. This is
previous research, rather than an ongoing project of mine. The Python workflow
supports inspection of EmotiBit physiological recordings through CSV loading,
time-window selection and sensor plotting.

The work continues to be used by Tom Gallagher in Professor Alan Marshall's
research group.

`Previous postdoctoral research` · `Physiological data` · `Python` · `pandas` · `Matplotlib`

**[Explore SonyEmotiBitAnalysis →](https://github.com/DavidBatty95/SonyEmotiBitAnalysis)**

<sub>The source repository is private and requires access. The illustration above is a schematic, not participant data. <a href="mailto:dwbatty@liverpool.ac.uk">Contact me about the research.</a></sub>

[↑ Back to top](#top)

---

## Technical focus

| Robotics & autonomy | Modelling & intelligence | Engineering |
| :--- | :--- | :--- |
| ROS / ROS 2 · SLAM · navigation | Gaussian processes · radiation mapping | Python · Linux · Docker |
| Humanoids · quadrupeds · social robots | Map abstraction · risk-aware planning | Simulation · benchmarking · reproducible experiments |
| Unitree G1 · Unitree Go2 · Pepper | Speech recognition · conversational AI | MuJoCo · RViz · system integration |
| Experimental sensing · wearable data | Physiological time series · pandas · Matplotlib | Responsive websites · freelance web development |

---

<div align="center">
  <strong>Let's connect on robotics, research collaboration and freelance web development.</strong><br>
  <a href="mailto:dwbatty@liverpool.ac.uk">dwbatty@liverpool.ac.uk</a> &nbsp; · &nbsp;
  <a href="https://uk.linkedin.com/in/david-batty">LinkedIn</a> &nbsp; · &nbsp;
  <a href="https://orcid.org/0009-0003-5375-421X">ORCID</a>
</div>
