#!/usr/bin/env python3
"""Build project-specific illustrations and provenance-linked profile previews."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess

from PIL import Image,ImageDraw,ImageFont,ImageSequence

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT/'assets'


def card(name,kicker,tagline,lines,accent,scene,steps,footer):
    text = ''.join(f'<text x="46" y="{192+i*30}" class="body">{line}</text>' for i,line in enumerate(lines))
    flow = ''.join(f'<g transform="translate({46+i*284} 349)"><text y="0" class="number">0{i+1}</text><text x="34" y="0" class="step">{step}</text></g>' for i,step in enumerate(steps))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-labelledby="title desc">
<title id="title">{name} — {tagline}</title>
<desc id="desc">{'. '.join(lines)}. Workflow: {', '.join(steps)}. Original illustrative schematic, not recorded robot motion or live measurements.</desc>
<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#091725"/><stop offset="1" stop-color="#132d40"/></linearGradient>
<linearGradient id="edge"><stop stop-color="{accent}"/><stop offset="1" stop-color="#1b3b50"/></linearGradient>
<radialGradient id="glow"><stop stop-color="{accent}" stop-opacity=".12"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse"><path d="M34 0H0V34" fill="none" stroke="#2a485d" stroke-width=".6"/></pattern>
</defs>
<style>
text {{font-family:Segoe UI,Helvetica,Arial,sans-serif}}
.body {{fill:#bdcfdd;font-size:21px}} .step {{fill:#eaf3fa;font-size:19px;font-weight:650}}
.number {{fill:{accent};font-size:16px;font-weight:700}} .label {{font-size:12px;fill:#a9bfce;letter-spacing:1px}}
.flow {{stroke-dasharray:7 9;animation:flow 4s linear infinite}}
.pulse {{animation:pulse 4s ease-in-out infinite}}
@keyframes flow {{to {{stroke-dashoffset:-64}}}} @keyframes pulse {{50% {{opacity:.35}}}}
@media(prefers-reduced-motion:reduce) {{* {{animation:none!important}}}}
</style>
<rect width="1200" height="420" rx="20" fill="url(#bg)"/>
<rect x="1" y="1" width="1198" height="418" rx="19" fill="none" stroke="#294558"/>
<path d="M24 1H1176" stroke="url(#edge)" stroke-width="3"/>
<rect x="624" y="20" width="554" height="282" fill="url(#grid)" opacity=".28"/>
<ellipse cx="920" cy="150" rx="280" ry="160" fill="url(#glow)"/>
<text x="46" y="48" fill="{accent}" font-size="13" font-weight="750" letter-spacing="2.3">{kicker}</text>
<text x="42" y="124" fill="#f3f8fc" font-size="67" font-weight="800" letter-spacing="-2">{name}</text>
<text x="46" y="160" fill="{accent}" font-size="23" font-weight="600">{tagline}</text>
{text}
{scene}
<path d="M46 308H1154" stroke="#2c475c"/>
{flow}
<text x="46" y="391" fill="#809cad" font-size="13">{footer}</text>
<text x="1154" y="391" text-anchor="end" fill="{accent}" font-size="14" font-weight="700">EXPLORE THE PROJECT ↗</text>
</svg>'''


GEOFF_SCENE = '''
<g transform="translate(641 10)">
 <path d="M10 235L275 105L528 224L270 290Z" fill="#153247" stroke="#31556b"/>
 <path d="M55 238L280 129M112 264L335 154M168 285L390 181M71 205L287 283M128 177L345 255M185 150L402 227" stroke="#24485e" fill="none"/>
 <path class="flow" d="M142 226Q195 260 255 221T417 225" stroke="#74e6cf" stroke-width="3" fill="none"/>
 <ellipse cx="277" cy="235" rx="58" ry="21" fill="#6fe0dc" opacity=".08"/>
 <ellipse class="pulse" cx="277" cy="235" rx="79" ry="28" fill="none" stroke="#6fe0dc" stroke-opacity=".5"/>
 <g stroke="#668499" stroke-width="6" stroke-linecap="round"><path d="M89 176V232M159 191V246M185 169V221M379 176V228M449 190V242M480 168V221"/></g>
 <path d="M67 164L117 140L196 169L148 194Z" fill="#96684d" stroke="#c79770"/>
 <path d="M359 162L408 138L488 167L441 192Z" fill="#96684d" stroke="#c79770"/>
 <path d="M389 163L411 152L452 167L430 179Z" fill="#547ee2" stroke="#a3c4ff" stroke-width="2"/>
 <g stroke-linecap="round" stroke-linejoin="round">
  <path d="M268 163L252 197L241 231M280 164L298 193L311 224" fill="none" stroke="#0b1726" stroke-width="17"/>
  <path d="M268 163L252 197L241 231M280 164L298 193L311 224" fill="none" stroke="#c5d9e4" stroke-width="11"/>
  <path d="M244 232L231 236M311 225L326 230" stroke="#82a3b9" stroke-width="10"/>
  <path d="M261 113L237 143L225 165M285 113L306 138L339 127" fill="none" stroke="#0b1726" stroke-width="15"/>
  <path d="M261 113L237 143L225 165M285 113L306 138L339 127" fill="none" stroke="#d2e3ed" stroke-width="9"/>
 </g>
 <path d="M254 104Q274 95 292 105L288 158Q272 174 257 157Z" fill="#d9e7ee" stroke="#91b0c3"/>
 <path d="M260 113H285L282 145H263Z" fill="#24495f"/>
 <circle class="pulse" cx="273" cy="121" r="5" fill="#73ebdb"/>
 <rect x="259" y="70" width="30" height="28" rx="9" fill="#dcebf1"/>
 <path d="M266 83H282" stroke="#132a3c" stroke-width="5" stroke-linecap="round"/>
 <path d="M329 107L350 97L370 107L350 117Z" fill="#ffc18e"/>
 <path d="M329 107V128L350 140V117Z" fill="#ec795e"/>
 <path d="M350 117L370 107V129L350 140Z" fill="#ad4947"/>
 <path d="M273 83L186 126M273 83L336 53" stroke="#72e8df" stroke-width="1" stroke-dasharray="3 5" opacity=".6"/>
 <g fill="#72e8df"><circle cx="186" cy="126" r="3"/><circle cx="336" cy="53" r="3"/><circle cx="200" cy="119" r="2"/><circle cx="325" cy="57" r="2"/></g>
 <text x="22" y="117" class="label">OBSERVED PICKUP</text><path d="M113 124V138" stroke="#668499"/>
 <text x="373" y="117" class="label">TARGET PAD</text><path d="M417 123V139" stroke="#668499"/>
 <text x="196" y="278" class="label">ILLUSTRATED WORKFLOW</text>
</g>'''


DOUGIE_SCENE = '''
<g transform="translate(642 8)">
 <path d="M10 228L267 102L526 220L269 289Z" fill="#162c40" stroke="#466078"/>
 <path d="M52 230L275 127M114 250L331 153M174 269L386 178M83 191L286 273M146 160L353 251" stroke="#28435a"/>
 <path d="M259 113V197M353 154V241M484 98V209" stroke="#59748b" stroke-width="7"/>
 <path d="M237 100L369 38L506 96L374 163Z" fill="#29475d" stroke="#7a98ac" stroke-width="2"/>
 <path d="M237 100V110L374 174V163M374 174L506 107V96" fill="#1c354a" stroke="#47677e"/>
 <path d="M372 163L471 213L423 237L324 186Z" fill="#5a6672" stroke="#94a6b2"/>
 <path d="M324 186L226 236L271 258L369 209Z" fill="#465e73" stroke="#94a6b2"/>
 <path d="M240 86L369 24L502 82M240 86V102M369 24V39M502 82V98M280 67V83M326 46V62M413 43V57M459 63V77" fill="none" stroke="#e8bf78" stroke-width="2"/>
 <ellipse cx="425" cy="105" rx="42" ry="19" fill="#ef8f61" opacity=".12"/>
 <ellipse class="pulse" cx="425" cy="105" rx="30" ry="14" fill="none" stroke="#efb879"/>
 <path d="M410 72Q424 65 438 72V103Q424 112 410 103Z" fill="#b78748" stroke="#f5ca83"/>
 <ellipse cx="424" cy="72" rx="14" ry="5" fill="#f2c87b"/>
 <text x="415" y="98" fill="#493b27" font-family="DejaVu Sans,sans-serif" font-size="22">☢</text>
 <g fill="#efb879" opacity=".65"><circle cx="384" cy="109" r="3"/><circle cx="395" cy="123" r="3"/><circle cx="418" cy="125" r="4"/><circle cx="447" cy="117" r="4"/><circle cx="464" cy="102" r="3"/><circle cx="459" cy="88" r="3"/></g>
 <g fill="#83cbd4" opacity=".7"><circle cx="318" cy="88" r="2"/><circle cx="336" cy="97" r="2"/><circle cx="354" cy="106" r="3"/><circle cx="349" cy="79" r="2"/><circle cx="368" cy="88" r="3"/></g>
 <path class="flow" d="M77 239L176 213L228 236L271 247L338 207L361 188L419 216L451 211L362 166L402 133" fill="none" stroke="#91d9d0" stroke-width="3"/>
 <circle cx="77" cy="239" r="12" fill="#183c4d" stroke="#91d9d0" stroke-width="2"/>
 <path d="M71 240L77 234L83 240V245H71Z" fill="#91d9d0"/>
 <text x="32" y="270" class="label">RETURN RESERVE</text>
 <g stroke-linecap="round" stroke-linejoin="round">
  <path d="M160 169L148 196L159 216M201 171L213 193L203 218" stroke="#1c2936" stroke-width="13" fill="none"/>
  <path d="M160 169L148 196L159 216M201 171L213 193L203 218" stroke="#88a6b9" stroke-width="7" fill="none"/>
  <path d="M141 180L130 206L139 228M183 187L194 211L185 232" stroke="#0a1725" stroke-width="14" fill="none"/>
  <path d="M141 180L130 206L139 228M183 187L194 211L185 232" stroke="#d4e4ec" stroke-width="8" fill="none"/>
 </g>
 <path d="M128 159L155 146L211 164L185 181Z" fill="#e3edf2" stroke="#9cb5c5"/>
 <path d="M128 159V176L185 198V181Z" fill="#86a7bc" stroke="#acbfcd"/>
 <path d="M185 181L211 164V180L185 198Z" fill="#24465c"/>
 <path d="M116 157L134 151L144 163L129 175L116 171Z" fill="#cfdee7"/>
 <circle cx="120" cy="163" r="4" fill="#122a3d"/>
 <path d="M173 144V133M166 133H180" stroke="#e6bc7b" stroke-width="3"/>
 <circle class="pulse" cx="173" cy="127" r="5" fill="#f2c87b"/>
 <path d="M173 124Q185 103 209 105M173 124Q188 91 225 95" fill="none" stroke="#e6bc7b" opacity=".6"/>
 <text x="292" y="282" class="label">MULTI-HEIGHT MAPPING</text>
 <text x="267" y="16" class="label">ILLUSTRATED FACILITY</text>
</g>'''


def font(size):
    return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',size)


def save_gif(frames,durations,path):
    sheet = Image.new('RGB',(1280,118))
    for i in range(10):
        tile = frames[round(i*(len(frames)-1)/9)].copy()
        tile.thumbnail((128,118))
        sheet.paste(tile,(i*128,0))
    palette = sheet.quantize(colors=192)
    encoded = [frame.quantize(palette=palette,dither=getattr(Image,'Dither',Image).NONE) for frame in frames]
    encoded[0].save(path,save_all=True,append_images=encoded[1:],duration=durations,loop=0,optimize=True,disposal=1)


def geoff_preview(path):
    frames,durations = [],[]
    with Image.open(path) as source:
        for frame in ImageSequence.Iterator(source):
            image = frame.convert('RGB')
            image = image.resize((640,590),getattr(Image,'Resampling',Image).LANCZOS)
            frames.append(image)
            durations.append(frame.info.get('duration',170))
    save_gif(frames,durations,ASSETS/'geoff-locomanipulation.gif')
    frames[0].save(ASSETS/'geoff-locomanipulation.png')


def dougie_preview(path):
    data = json.loads(path.read_text())
    run = next(row for row in data['runs'] if row['seed']==3 and row['round_trip'])
    points = run['points']
    bounds = [(math.floor(min(p[i] for p in points)/3)*3,
               math.ceil(max(p[i] for p in points)/3)*3) for i in (1,2)]
    (xmin,xmax),(ymin,ymax) = bounds
    def raw_project(p):
        _,x,y,z = p
        return (20*x-13*y,7*x+8*y-53*z)
    corners = [(0,x,y,z) for x in (xmin,xmax) for y in (ymin,ymax) for z in (0.,2.4)]
    projected = [raw_project(p) for p in points+corners]
    lo = [min(p[i] for p in projected) for i in (0,1)]
    hi = [max(p[i] for p in projected) for i in (0,1)]
    scale = min(580/(hi[0]-lo[0]),275/(hi[1]-lo[1]))
    def project(p):
        x,y = raw_project(p)
        return (320+(x-(lo[0]+hi[0])/2)*scale,227.5+(y-(lo[1]+hi[1])/2)*scale)
    trajectory = [project(p) for p in points]
    frames = []
    for index in range(90):
        end = max(1,round(index*(len(points)-1)/89))
        t,x,y,z = points[end]
        image = Image.new('RGB',(640,590),'#0a1928')
        draw = ImageDraw.Draw(image)
        draw.text((24,16),'DOUGIE / EXPLORE + RETURN',font=font(24),fill='#eef5fb')
        draw.text((24,51),'ACTUAL DETECTOR POSITIONS · ACCELERATED REPLAY',font=font(13),fill='#efc68a')
        for height in (0.,2.4):
            corners = [project((0,a,b,height)) for a,b in ((xmin,ymin),(xmax,ymin),(xmax,ymax),(xmin,ymax))]
            draw.polygon(corners,outline='#345269')
            for value in range(xmin+3,xmax,3):
                draw.line([project((0,value,ymin,height)),project((0,value,ymax,height))],fill='#1d3549')
            for value in range(ymin+3,ymax,3):
                draw.line([project((0,xmin,value,height)),project((0,xmax,value,height))],fill='#1d3549')
        draw.text((18,106),'UPPER FLOOR  /  2.4 m',font=font(13),fill='#efc68a')
        draw.text((18,344),'GROUND FLOOR',font=font(13),fill='#8cb3c9')
        for a,b in zip(trajectory[:end],trajectory[1:end+1]):
            draw.line((a,b),fill='#72ded5',width=3)
        px,py = trajectory[end]
        draw.ellipse((px-7,py-7,px+7,py+7),fill='#f4c981',outline='#fff2d5',width=2)
        home = trajectory[0]
        draw.ellipse((home[0]-5,home[1]-5,home[0]+5,home[1]+5),outline='#b3d5ee',width=2)
        draw.text((24,390),f'MISSION TIME  {t:,.0f} s',font=font(18),fill='#eef5fb')
        draw.text((350,390),f'DETECTOR HEIGHT  {z:.2f} m',font=font(16),fill='#efc68a')
        draw.text((24,424),'HEIGHT HISTORY',font=font(12),fill='#8eabbe')
        chart = [(24+590*p[0]/points[-1][0],505-20*p[3]) for p in points[:end+1]]
        draw.line((24,505,614,505),fill='#345269')
        if len(chart)>1:
            draw.line(chart,fill='#efc68a',width=2)
        draw.text((24,525),f'RECORDED OUTCOME: upper floor → home · {run["dose_usv"]:.2f} / 5 µSv',font=font(15),fill='#a9e3d5')
        draw.text((24,556),'Seed 3 · one facility layout · telemetry, not video or a GP field',font=font(12),fill='#8eabbe')
        frames.append(image)
    save_gif(frames,[110]*89+[2500],ASSETS/'dougie-multilevel.gif')
    frames[-1].save(ASSETS/'dougie-multilevel.png')
    return {key:run[key] for key in ('run','seed','round_trip','duration_s','dose_usv','measurement_sha256','summary_sha256')}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geoff',type=Path,required=True)
    parser.add_argument('--dougie',type=Path,required=True)
    args = parser.parse_args()
    (ASSETS/'geoff-showcase.svg').write_text(card('Geoff-Sim','01 / EMBODIED AUTONOMY','Perceive. Pick up. Walk. Deliver.',
        ['Sensor-driven humanoid locomanipulation.','RGB-D pickup, loaded walking and human-aware','planning in one inspectable research platform.'],
        '#76e7d2',GEOFF_SCENE,['Observe + map','Approach + dock','Pick up + carry','Place + verify'],
        'UNITREE G1 · ROS 2 HUMBLE · MUJOCO · ONBOARD PERCEPTION'))
    (ASSETS/'dougie-showcase.svg').write_text(card('Dougie-Sim','02 / RISK-AWARE EXPLORATION','Explore the unknown. Budget the way home.',
        ['Quadruped exploration with radiation constraints.','Online Gaussian process mapping, observed','terrain and dose-aware return reasoning.'],
        '#f2c487',DOUGIE_SCENE,['Sense + explore','Infer the field','Plan with dose','Return home'],
        'UNITREE GO2 · POISSON SENSING · SPARSE GP · MULTI-HEIGHT TERRAIN'))
    geoff = args.geoff/'docs/media/locomanipulation/pickup-and-lift.gif'
    dougie = args.dougie/'docs/media/dougie/facility-telemetry.json'
    geoff_preview(geoff)
    selected = dougie_preview(dougie)
    sources = []
    for identity,repo,path in (('DavidBatty95/Geoff-Sim',args.geoff,geoff),('DavidBatty95/Dougie-Sim',args.dougie,dougie)):
        relative = str(path.relative_to(repo))
        sources.append(dict(repository=identity,path=relative,sha256=sha(path),
            head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip(),
            source_dirty=bool(subprocess.check_output(['git','status','--porcelain','--',relative],cwd=repo,text=True))))
    files = ['geoff-showcase.svg','dougie-showcase.svg','geoff-locomanipulation.gif','geoff-locomanipulation.png','dougie-multilevel.gif','dougie-multilevel.png']
    (ASSETS/'project-showcase-sources.json').write_text(json.dumps(dict(
        scope='Original schematic project cards; Geoff actual captured excerpt; Dougie actual downsampled telemetry replay',
        sources=sources,dougie_selected_run=selected,
        geoff_scope='Pickup/lift excerpt from 20261014T164500Z-readme-settling; source attempt later fell, no completed delivery',
        files=[dict(file='assets/'+name,sha256=sha(ASSETS/name),bytes=(ASSETS/name).stat().st_size) for name in files]),indent=2)+'\n')
    print('Built two project cards and two source-linked animated previews.')


if __name__=='__main__':
    main()
