/* Decorative local navigation simulation. No dependencies or live robot data. */
(() => {
  'use strict';
  const canvas = document.getElementById('robot-world');
  const ctx = canvas.getContext('2d');
  const field = document.getElementById('set-goal');
  const toggle = document.getElementById('motion-toggle');
  const stateLabel = document.getElementById('planner-state');
  const countLabel = document.getElementById('waypoint-count');
  const feedback = document.getElementById('map-feedback');
  if (!ctx) {
    stateLabel.textContent = 'CANVAS UNAVAILABLE';
    field.disabled = true;
    toggle.disabled = true;
    return;
  }
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let paused = reducedMotion.matches;
  let width, height, cell, cols, rows, blocked, robot, goal, route = [], trail = [];
  let reached = 0, heading = -Math.PI / 2, clock = 0, lastTime = 0, frame = 0;
  let arena;

  const index = (x, y) => y * cols + x;
  const centre = point => ({ x: (point.x + .5) * cell, y: (point.y + .5) * cell });
  const tile = point => ({ x: Math.max(0, Math.min(cols - 1, Math.floor(point.x / cell))), y: Math.max(0, Math.min(rows - 1, Math.floor(point.y / cell))) });
  const free = (x, y) => x >= arena.left && x < arena.right && y >= arena.top && y < arena.bottom && !blocked.has(index(x, y));

  // A* on a four-connected occupancy grid. Neighbours cannot cut obstacle corners.
  function plan(start, end) {
    const startId = index(start.x, start.y), endId = index(end.x, end.y);
    const open = new Set([startId]), cameFrom = new Map(), costs = new Map([[startId, 0]]);
    const distance = id => Math.abs(id % cols - end.x) + Math.abs(Math.floor(id / cols) - end.y);
    const scores = new Map([[startId, distance(startId)]]);
    while (open.size) {
      let current, best = Infinity;
      for (const id of open) {
        if (scores.get(id) < best) { current = id; best = scores.get(id); }
      }
      if (current === endId) {
        const path = [];
        while (current !== startId) {
          path.unshift(centre({ x: current % cols, y: Math.floor(current / cols) }));
          current = cameFrom.get(current);
        }
        return path;
      }
      open.delete(current);
      const x = current % cols, y = Math.floor(current / cols);
      for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const nx = x + dx, ny = y + dy;
        if (!free(nx, ny)) continue;
        const next = index(nx, ny), cost = costs.get(current) + 1;
        if (cost < (costs.get(next) ?? Infinity)) {
          cameFrom.set(next, current); costs.set(next, cost);
          scores.set(next, cost + distance(next)); open.add(next);
        }
      }
    }
    return null;
  }

  function setGoal(destination, announce = false) {
    if (!free(destination.x, destination.y)) {
      if (announce) feedback.textContent = 'That location is occupied. Choose an open area of the map.';
      return false;
    }
    const start = tile(robot), path = plan(start, destination);
    if (!path || !path.length) {
      if (announce) feedback.textContent = 'Choose another open location for the robot to explore.';
      return false;
    }
    // Rejoin the current cell centre before following a replanned route.
    // This preserves collision-free grid edges when redirected mid-step.
    route = [centre(start), ...path];
    goal = centre(destination);
    if (announce) feedback.textContent = paused ? 'New route planned. Resume motion to follow it.' : 'New destination set. The robot is following its planned route.';
    return true;
  }

  function randomGoal() {
    for (let attempt = 0; attempt < 120; attempt++) {
      const destination = {
        x: arena.left + Math.floor(Math.random() * (arena.right - arena.left)),
        y: arena.top + Math.floor(Math.random() * (arena.bottom - arena.top))
      };
      if (Math.hypot(destination.x * cell - robot.x, destination.y * cell - robot.y) > cell * 3 && setGoal(destination)) return true;
    }
    // A deterministic fallback also covers unusually small browser viewports.
    for (let y = arena.top; y < arena.bottom; y++) {
      for (let x = arena.left; x < arena.right; x++) if (setGoal({ x, y })) return true;
    }
    return false;
  }

  function resize() {
    width = window.innerWidth; height = window.innerHeight;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(width * dpr); canvas.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cell = width < 760 ? 25 : 32;
    cols = Math.ceil(width / cell); rows = Math.ceil(height / cell);
    const rect = field.getBoundingClientRect();
    // Fit the navigation world to the clear hero region while it is on screen.
    const visible = rect.bottom > 120 && rect.top < height - 100;
    const left = visible ? Math.ceil((rect.left + 20) / cell) : Math.max(1, Math.floor(cols * .52));
    const right = visible ? Math.floor((rect.right - 20) / cell) : cols - 1;
    const top = visible ? Math.max(1, Math.ceil((rect.top + 42) / cell)) : 2;
    const bottom = visible ? Math.min(rows - 1, Math.floor((rect.bottom - 44) / cell)) : rows - 2;
    // On narrow/short screens retain enough room for the decorative robot.
    arena = { left: Math.min(left, cols - 4), right: Math.max(right, Math.min(left, cols - 4) + 3), top: Math.min(top, rows - 4), bottom: Math.max(bottom, Math.min(top, rows - 4) + 3) };
    blocked = new Set();
    const aw = arena.right - arena.left, ah = arena.bottom - arena.top;
    // Sparse fixed obstacle islands, with open perimeter corridors.
    for (const [fx, fy, fw, fh] of [[.22, .2, .13, .23], [.61, .12, .17, .2], [.46, .65, .13, .2], [.78, .55, .1, .14]]) {
      const ox = arena.left + Math.floor(aw * fx), oy = arena.top + Math.floor(ah * fy);
      for (let x = ox; x < Math.min(arena.right - 1, ox + Math.max(1, Math.floor(aw * fw))); x++) {
        for (let y = oy; y < Math.min(arena.bottom - 1, oy + Math.max(1, Math.floor(ah * fh))); y++) blocked.add(index(x, y));
      }
    }
    robot = centre({ x: arena.left, y: arena.bottom - 1 });
    route = []; trail = []; goal = null;
    randomGoal(); draw();
  }

  function line(points, colour, lineWidth, dashed = false) {
    if (!points.length) return;
    ctx.beginPath(); ctx.moveTo(points[0].x, points[0].y);
    for (const point of points.slice(1)) ctx.lineTo(point.x, point.y);
    ctx.strokeStyle = colour; ctx.lineWidth = lineWidth; ctx.setLineDash(dashed ? [4, 7] : []); ctx.stroke(); ctx.setLineDash([]);
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);
    ctx.strokeStyle = '#9fbcd00b'; ctx.lineWidth = 1;
    ctx.beginPath();
    for (let x = 0; x <= width; x += cell) { ctx.moveTo(x, 0); ctx.lineTo(x, height); }
    for (let y = 0; y <= height; y += cell) { ctx.moveTo(0, y); ctx.lineTo(width, y); }
    ctx.stroke();
    for (const id of blocked) {
      const x = (id % cols) * cell, y = Math.floor(id / cols) * cell;
      ctx.fillStyle = '#18354dd9'; ctx.fillRect(x + 2, y + 2, cell - 4, cell - 4);
      ctx.strokeStyle = '#80bfff38'; ctx.strokeRect(x + 2, y + 2, cell - 4, cell - 4);
      ctx.fillStyle = '#80bfff48'; ctx.fillRect(x + cell / 2 - 1, y + cell / 2 - 1, 2, 2);
    }
    line(trail, '#80bfff55', 1.5);
    line([robot, ...route], '#5eead47a', 1.5, true);
    if (goal) {
      const pulse = 13 + Math.sin(clock * 2) * 3;
      ctx.strokeStyle = '#5eead436'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(goal.x, goal.y, pulse, 0, Math.PI * 2); ctx.stroke();
      ctx.strokeStyle = '#5eead4cc'; ctx.beginPath();
      ctx.moveTo(goal.x - 5, goal.y); ctx.lineTo(goal.x + 5, goal.y);
      ctx.moveTo(goal.x, goal.y - 5); ctx.lineTo(goal.x, goal.y + 5); ctx.stroke();
    }
    // LiDAR-style sensing rings and rays, clipped to the map boundary.
    ctx.save(); ctx.beginPath(); ctx.rect(arena.left * cell, arena.top * cell, (arena.right - arena.left) * cell, (arena.bottom - arena.top) * cell); ctx.clip();
    for (const radius of [42, 76, 112]) {
      ctx.beginPath(); ctx.arc(robot.x, robot.y, radius, 0, Math.PI * 2);
      ctx.strokeStyle = '#5eead412'; ctx.stroke();
    }
    for (let i = 0; i < 20; i++) {
      const angle = i * Math.PI / 10 + clock * .14;
      let range = 90;
      for (let d = 14; d < 90; d += 4) {
        const p = tile({ x: robot.x + Math.cos(angle) * d, y: robot.y + Math.sin(angle) * d });
        if (!free(p.x, p.y)) { range = d; break; }
      }
      const end = { x: robot.x + Math.cos(angle) * range, y: robot.y + Math.sin(angle) * range };
      line([robot, end], '#5eead40d', 1);
      ctx.fillStyle = '#5eead46b'; ctx.fillRect(end.x - 1, end.y - 1, 2, 2);
    }
    ctx.restore();
    ctx.save(); ctx.translate(robot.x, robot.y); ctx.rotate(heading);
    ctx.shadowColor = '#5eead4'; ctx.shadowBlur = 16;
    ctx.fillStyle = '#0b1424'; ctx.strokeStyle = '#5eead4'; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.roundRect(-11, -9, 22, 18, 4); ctx.fill(); ctx.stroke();
    ctx.shadowBlur = 0; ctx.fillStyle = '#80bfff';
    ctx.fillRect(-8, -13, 7, 3); ctx.fillRect(3, -13, 7, 3);
    ctx.fillRect(-8, 10, 7, 3); ctx.fillRect(3, 10, 7, 3);
    ctx.fillStyle = '#5eead4'; ctx.beginPath(); ctx.arc(4, 0, 3, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.moveTo(13, -4); ctx.lineTo(18, 0); ctx.lineTo(13, 4); ctx.stroke(); ctx.restore();
    stateLabel.textContent = paused ? 'PAUSED' : 'FOLLOWING ROUTE';
    countLabel.textContent = String(reached).padStart(3, '0');
  }

  function tick(now) {
    frame = 0;
    if (paused || document.hidden) return;
    const dt = Math.min((now - (lastTime || now)) / 1000, .05);
    lastTime = now; clock += dt;
    if (route.length) {
      const next = route[0], dx = next.x - robot.x, dy = next.y - robot.y, distance = Math.hypot(dx, dy);
      const step = dt * 43;
      if (distance <= step) {
        robot = { ...next }; route.shift();
        if (!route.length) { reached++; randomGoal(); }
      } else {
        heading = Math.atan2(dy, dx);
        robot.x += dx / distance * step; robot.y += dy / distance * step;
      }
      if (!trail.length || Math.hypot(robot.x - trail[trail.length - 1].x, robot.y - trail[trail.length - 1].y) > 5) {
        trail.push({ ...robot }); if (trail.length > 180) trail.shift();
      }
    }
    draw(); frame = requestAnimationFrame(tick);
  }

  function syncMotion() {
    cancelAnimationFrame(frame); frame = 0; lastTime = 0;
    toggle.setAttribute('aria-pressed', String(paused));
    toggle.innerHTML = paused ? 'Resume motion <span aria-hidden="true">▷</span>' : 'Pause motion <span aria-hidden="true">Ⅱ</span>';
    draw();
    if (!paused && !document.hidden) frame = requestAnimationFrame(tick);
  }

  field.addEventListener('click', event => {
    if (event.detail === 0) {
      randomGoal(); feedback.textContent = 'New destination selected and route planned.';
    } else setGoal(tile({ x: event.clientX, y: event.clientY }), true);
    draw();
  });
  toggle.addEventListener('click', () => { paused = !paused; syncMotion(); });
  reducedMotion.addEventListener('change', event => { paused = event.matches; syncMotion(); });
  document.addEventListener('visibilitychange', syncMotion);
  let resizeTimer;
  window.addEventListener('resize', () => { clearTimeout(resizeTimer); resizeTimer = setTimeout(resize, 120); });
  // Reposition the world when the hero enters/leaves the viewport, without
  // continuously resetting the robot as the reader scrolls.
  const observer = new IntersectionObserver(resize, { threshold: [0, .5, 1] });
  observer.observe(field);
  resize(); syncMotion();
})();
