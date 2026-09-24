/* did. proposals gate
 * Serves the static proposal decks and puts a per-deck password in front of the ones listed in PASSWORDS.
 * A correct password sets a signed, HttpOnly cookie scoped to that deck's folder for 30 days.
 */

const COOKIE_DAYS = 30;
const NOINDEX = { 'X-Robots-Tag': 'noindex, nofollow', 'Cache-Control': 'private, no-store' };

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function gatePage(title, next, failed) {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Private proposal · did.</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600&family=Hanken+Grotesk:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>
  :root{--bg:#F4F4F3;--lift:#FFFFFF;--fg:#141018;--silver:#5C5B67;--dim:#6E6D78;--violet:#8366FF;--hair:rgba(20,19,24,0.12)}
  *{box-sizing:border-box;margin:0;padding:0}
  body{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px 16px;color:var(--fg);font-family:'Hanken Grotesk',sans-serif;-webkit-font-smoothing:antialiased;
    background:var(--bg);background-image:radial-gradient(120% 92% at 50% 112%,rgba(131,102,255,0.18) 0%,rgba(231,231,235,0.92) 40%,var(--bg) 78%)}
  .card{width:100%;max-width:440px;background:var(--lift);border:1px solid var(--hair);border-radius:20px;padding:36px 32px;box-shadow:0 1px 2px rgba(20,19,24,0.04),0 10px 30px rgba(20,19,24,0.06)}
  .mk{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:34px;letter-spacing:-0.045em;line-height:1}
  .mk .dot{color:var(--violet)}
  .k{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.24em;text-transform:uppercase;color:var(--violet);margin-top:26px}
  h1{font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:26px;letter-spacing:-0.03em;line-height:1.12;margin-top:10px}
  p{color:var(--silver);font-size:15px;line-height:1.5;margin-top:10px}
  label{display:block;font-size:13px;font-weight:600;margin-top:22px}
  input[type=password]{width:100%;margin-top:8px;padding:13px 14px;font:inherit;font-size:16px;border:1px solid rgba(20,19,24,0.3);border-radius:12px;background:#fff;color:var(--fg)}
  input[type=password]:focus{outline:2px solid var(--violet);outline-offset:1px;border-color:transparent}
  button{width:100%;margin-top:14px;padding:14px;border:0;border-radius:999px;background:var(--fg);color:var(--bg);font:inherit;font-weight:600;font-size:15px;cursor:pointer}
  button:hover{box-shadow:0 12px 30px rgba(0,0,0,0.25)}
  .err{margin-top:12px;color:#B3261E;font-size:14px;line-height:1.4}
  .fine{margin-top:22px;font-size:12px;color:var(--dim)}
  @media (max-width:480px){.card{padding:28px 22px}}
</style>
</head>
<body>
<form class="card" method="post" action="">
  <div class="mk">did<span class="dot">.</span></div>
  <div class="k">Private proposal</div>
  <h1>${esc(title)}</h1>
  <p>This page was prepared for one company. Enter the password from Nas's email to open it.</p>
  <label for="password">Password</label>
  <input id="password" name="password" type="password" autocomplete="current-password" autofocus required>
  <input type="hidden" name="next" value="${esc(next)}">
  <button type="submit">Open the proposal</button>
  ${failed ? '<div class="err">That password did not match. Check the email and try again.</div>' : ''}
  <p class="fine">Prepared by Do It Digital · doitdigital.agency</p>
</form>
</body>
</html>`;
}

async function hmacHex(secret, message) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(message));
  return Array.from(new Uint8Array(sig), (b) => b.toString(16).padStart(2, '0')).join('');
}

function timingSafeEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function readCookie(request, name) {
  const header = request.headers.get('Cookie') || '';
  for (const part of header.split(';')) {
    const [k, ...rest] = part.trim().split('=');
    if (k === name) return rest.join('=');
  }
  return null;
}

function deckConfig(env, slug) {
  let map = {};
  try { map = JSON.parse(env.PASSWORDS || '{}'); } catch (e) { map = {}; }
  const entry = map[slug];
  if (!entry) return null;
  if (typeof entry === 'string') return { password: entry, title: 'A proposal from Do It Digital' };
  if (entry && typeof entry.password === 'string') return { password: entry.password, title: entry.title || 'A proposal from Do It Digital' };
  return null;
}

function withHeaders(response, extra) {
  const r = new Response(response.body, response);
  for (const [k, v] of Object.entries(extra)) r.headers.set(k, v);
  return r;
}

function safeNext(candidate, slug) {
  const fallback = `/${slug}/`;
  if (typeof candidate !== 'string') return fallback;
  // same-origin path inside this deck only: no scheme, no protocol-relative, no other folder
  if (!candidate.startsWith(`/${slug}/`) || candidate.startsWith('//') || /[\r\n]/.test(candidate)) return fallback;
  return candidate;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    // Cookies are Secure-only, so plain HTTP can never unlock a deck: always move to HTTPS first.
    if (url.protocol === 'http:') {
      url.protocol = 'https:';
      return Response.redirect(url.toString(), 301);
    }
    const segments = url.pathname.split('/').filter(Boolean);

    // Root: nothing to list. Send people to the main site.
    if (segments.length === 0) return Response.redirect('https://doitdigital.agency/', 302);

    const slug = segments[0];
    // Only plain folder names are decks; nothing dot- or underscore-prefixed is ever served.
    if (!/^[a-z0-9][a-z0-9-]{0,63}$/.test(slug)) return new Response('Not found', { status: 404, headers: NOINDEX });

    const cfg = deckConfig(env, slug);
    if (!cfg || !env.COOKIE_SECRET) {
      // Open deck (or the gate is not configured yet): serve the static file.
      const res = await env.ASSETS.fetch(request);
      return withHeaders(res, { 'X-Robots-Tag': 'noindex, nofollow' });
    }

    const cookieName = `did_pp_${slug}`;
    // The token binds the deck and its current password, so changing the password locks everyone out again.
    const expected = await hmacHex(env.COOKIE_SECRET, `${slug}|${cfg.password}`);

    if (request.method === 'POST') {
      let given = '';
      let next = '';
      try {
        const form = await request.formData();
        given = String(form.get('password') || '').trim();
        next = String(form.get('next') || '');
      } catch (e) { /* not a form post */ }
      const givenSig = await hmacHex(env.COOKIE_SECRET, `${slug}|${given}`);
      if (given && timingSafeEqual(givenSig, expected)) {
        const headers = new Headers(NOINDEX);
        headers.set('Location', safeNext(next, slug));
        headers.append('Set-Cookie', `${cookieName}=${expected}; Path=/${slug}/; Max-Age=${COOKIE_DAYS * 86400}; HttpOnly; Secure; SameSite=Lax`);
        return new Response(null, { status: 303, headers });
      }
      return new Response(gatePage(cfg.title, url.pathname + url.search, true), { status: 401, headers: { 'Content-Type': 'text/html; charset=utf-8', ...NOINDEX } });
    }

    const cookie = readCookie(request, cookieName);
    if (cookie && timingSafeEqual(cookie, expected)) {
      const res = await env.ASSETS.fetch(request);
      return withHeaders(res, NOINDEX);
    }

    // Not unlocked. Pages get the gate; sub-resources get a bare 401 so nothing leaks.
    const wantsHtml = (request.headers.get('Accept') || '').includes('text/html') || url.pathname.endsWith('/') || url.pathname.endsWith('.html');
    if (request.method === 'GET' && wantsHtml) {
      return new Response(gatePage(cfg.title, url.pathname + url.search, false), { status: 401, headers: { 'Content-Type': 'text/html; charset=utf-8', ...NOINDEX } });
    }
    return new Response('Unauthorized', { status: 401, headers: NOINDEX });
  },
};
