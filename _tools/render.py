#!/usr/bin/env python3
"""Render every slide of a deck at 1920x1080 with headless Chrome and report overflow.
Chrome on this Mac writes its output and then never exits, so we poll for the output and kill it.
Usage: render.py <deck-folder> [slide numbers...]"""
import subprocess, sys, pathlib, re, urllib.parse, time, os, signal, shutil

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
folder = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path('/private/tmp/claude-501/-Users-Nas-Proposal-Do-It-Digital/118b6777-77b0-41e8-9ef6-944cdff4244a/scratchpad/renders') / folder.name
out.mkdir(parents=True, exist_ok=True)
html = (folder / 'index.html').read_text(encoding='utf-8')
n = html.count('<section class="slide')
wanted = [int(a) for a in sys.argv[2:]] or list(range(1, n + 1))
url_base = 'file://' + urllib.parse.quote(str(folder / 'index.html'))

def chrome(args, profile, done, timeout=40):
    """Start Chrome, wait until done() is true (or timeout), then kill it."""
    log = open(profile + '.out', 'w')
    p = subprocess.Popen([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check',
                          '--window-size=1920,1080', '--timeout=9000', f'--user-data-dir={profile}'] + args,
                         stdout=log, stderr=subprocess.DEVNULL, start_new_session=True)
    t0 = time.time()
    ok = False
    while time.time() - t0 < timeout:
        if done():
            ok = True; time.sleep(0.6); break
        time.sleep(0.4)
    try: os.killpg(os.getpgid(p.pid), signal.SIGKILL)
    except Exception: p.kill()
    p.wait()
    log.close()
    shutil.rmtree(profile, ignore_errors=True)
    return ok

for s in wanted:
    url = f'{url_base}?s={s}&qa=1'
    shot = out / f's{s:02d}.png'
    if shot.exists(): shot.unlink()
    prof = f'/tmp/cr-shot-{s}'
    ok1 = chrome([f'--screenshot={shot}', url], prof, lambda: shot.exists() and shot.stat().st_size > 0)
    prof2 = f'/tmp/cr-dom-{s}'
    domfile = pathlib.Path(prof2 + '.out')
    def dom_done():
        try: return '</html>' in domfile.read_text(errors='ignore')
        except Exception: return False
    ok2 = chrome(['--dump-dom', url], prof2, dom_done)
    dom = domfile.read_text(errors='ignore') if domfile.exists() else ''
    m = re.search(r'<title>([^<]*)</title>', dom)
    title = m.group(1) if m else 'NO TITLE'
    print(f'slide {s:02d}: {title}   -> {shot.name} {"ok" if ok1 else "MISSING"}{"" if ok2 else " (dom timeout)"}', flush=True)
    for f in (prof + '.out', prof2 + '.out'):
        try: os.unlink(f)
        except Exception: pass
