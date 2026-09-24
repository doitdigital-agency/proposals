#!/usr/bin/env python3
"""Build hypr/index.html (LinkedIn Outbound proposal for HYPR Digital Marketing)
from the generic Voice System deck's head + CSS, with new slides and scripts."""
import re, pathlib

ROOT = pathlib.Path('/Users/Nas/Proposal Do It Digital')
SRC = (ROOT / 'voice-system' / 'index.html').read_text(encoding='utf-8')
OUT = ROOT / 'hypr' / 'index.html'

RATE = 1.33               # GBP to USD, indicative, 23 Sep 2026 (open.er-api.com 1.3345)
RET_GBP = 1100            # retainer every 28 days
CYCLES = 3
RET_GBP_TOTAL = RET_GBP * CYCLES          # 3,300
RET_USD_TOTAL = 4400                      # 3,300 x 1.33 = 4,389, rounded for the calculator
DATE = '24 September 2026'

head = SRC.split('</style>')[0]
# ---- head metadata -------------------------------------------------------
head = head.replace('<title>The Voice System · a LinkedIn founder-voice system by did.</title>',
                    '<title>LinkedIn Outbound for HYPR · a proposal by did.</title>')
head = re.sub(r'<meta name="description" content="[^"]*">',
              '<meta name="description" content="LinkedIn Outbound for HYPR Digital Marketing: positioning and graphics rebuilt, a named target list, warm and cold sequences in Pritpal\'s voice, and discovery calls booked into Jay\'s calendar. GBP 1,100 every 28 days plus 50% of the first invoice.">', head)
head = head.replace('<meta property="og:title" content="The Voice System by did.">',
                    '<meta property="og:title" content="LinkedIn Outbound for HYPR, by did.">')
# the slide footer text lives in a CSS content string
head = head.replace('The Voice System', 'LinkedIn Outbound')
head = re.sub(r'<meta property="og:description" content="[^"]*">',
              '<meta property="og:description" content="A 12-week LinkedIn outbound system for HYPR Digital Marketing, prepared by Do It Digital.">', head)

EXTRA_CSS = r"""
  /* ---- HYPR deck additions ---- */
  .qa .reveal{opacity:1!important;transform:none!important;transition:none!important}
  .qa .navmark .l:not(.k),.qa .navmark .sp{animation:none;max-width:0;opacity:0}
  .nav-for img.wm{width:auto;height:22px;border-radius:0;background:none;padding:0}
  .lockup img.wm{width:auto;height:44px;border-radius:0;box-shadow:none}
  .lockup .x{font-family:var(--mono);font-size:15px;color:var(--dim)}
  .cover h1{max-width:17ch}

  /* positioning slide */
  .pos{display:grid;grid-template-columns:1.08fr 0.92fr;gap:24px;margin-top:18px;align-items:start}
  .prof{overflow:hidden;position:relative;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.9);background:#fff}
  .prof .banner{position:relative;height:148px;background:#0b0b0b;color:#fff;padding:20px 26px;display:flex;flex-direction:column;justify-content:flex-start;gap:8px;overflow:hidden}
  .prof .banner::after{content:"";position:absolute;right:-60px;bottom:-90px;width:260px;height:260px;border-radius:50%;background:rgba(88,224,224,0.14)}
  .prof .banner .hl{position:relative;z-index:1;font-family:var(--disp);font-weight:600;font-size:23px;line-height:1.12;letter-spacing:-0.02em;max-width:19ch}
  .prof .banner .hl i{font-style:normal;background:#58e0e0;color:#0b0b0b;padding:0 6px}
  .prof .banner .sub{position:relative;z-index:1;font-size:12.5px;color:rgba(255,255,255,0.78);letter-spacing:0.01em;max-width:60ch;white-space:nowrap}
  .prof .banner .lg{position:absolute;right:18px;top:16px;z-index:1;background:#fff;border-radius:8px;padding:7px 11px 5px}
  .prof .banner .lg img{height:26px;width:auto}
  .prof .banner .bstrip{position:absolute;right:20px;bottom:12px;left:auto;width:auto;z-index:1;font-family:var(--mono);font-size:9.5px;letter-spacing:0.14em;text-transform:uppercase;color:rgba(255,255,255,0.6);white-space:nowrap}
  body.staged [data-title="The 12-week outcome"] .pgrid .browser img{height:172px}
  body.staged [data-title="The 12-week outcome"] .outs{gap:7px}
  body.staged [data-title="The 12-week outcome"] .outs li{padding:8px 14px 8px 50px}
  body.staged [data-title="The 12-week outcome"] .outs li::before{top:10px}
  body.staged [data-title="The 12-week outcome"] .note{margin-top:12px}
  body.staged [data-title="How we have helped others"] .proof3{margin-top:16px}
  body.staged [data-title="How we have helped others"] .qstrip{margin-top:10px}
  body.staged .prices .big{font-size:48px}
  .prices .big span{display:block;margin:8px 0 0}
  .prof .head{padding:0 26px 16px;position:relative}
  .prof .av{width:92px;height:92px;border-radius:50%;background:#e9e5df;border:4px solid #fff;margin-top:-46px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:26px;color:#4b4b4b;position:relative;z-index:2}
  .prof .nm{font-size:21px;font-weight:600;margin-top:8px;display:flex;align-items:center;gap:8px}
  .prof .nm i{font-style:normal;font-size:11px;color:rgba(0,0,0,0.6);font-weight:400}
  .prof .hd{font-size:14.5px;line-height:1.4;margin-top:3px;color:rgba(0,0,0,0.9)}
  .prof .meta{font-size:12.5px;color:rgba(0,0,0,0.6);margin-top:5px}
  .prof .btns{display:flex;gap:8px;margin-top:10px}
  .prof .btns span{border-radius:999px;padding:5px 14px;font-size:13px;font-weight:600;border:1px solid #0a66c2;color:#0a66c2}
  .prof .btns span.p{background:#0a66c2;color:#fff}
  .prof .feat{padding:12px 26px 18px;border-top:1px solid rgba(0,0,0,0.08)}
  .prof .feat .fk{font-size:13px;font-weight:600;margin-bottom:9px}
  .prof .fcards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
  .prof .fc{border:1px solid rgba(0,0,0,0.1);border-radius:8px;overflow:hidden;background:#fff}
  .prof .fc .im{height:66px;background:#0b0b0b;color:#fff;padding:9px 11px;font-family:var(--disp);font-weight:600;font-size:12.5px;line-height:1.2;display:flex;align-items:flex-end;position:relative;overflow:hidden}
  .prof .fc .im::before{content:"";position:absolute;left:0;top:0;width:100%;height:5px;background:#58e0e0}
  .prof .fc .im.c{background:#58e0e0;color:#0b0b0b}.prof .fc .im.c::before{background:#0b0b0b}
  .prof .fc .im.w{background:#fff;color:#0b0b0b;border-bottom:1px solid rgba(0,0,0,0.08)}
  .prof .fc .cap{font-size:11px;color:rgba(0,0,0,0.6);padding:7px 11px 8px;line-height:1.35}
  .prof .tag{position:absolute;right:16px;top:158px;z-index:3;font-family:var(--mono);font-size:9.5px;letter-spacing:0.16em;text-transform:uppercase;color:var(--violet);background:var(--lift);border:1px solid var(--hair);border-radius:999px;padding:4px 9px}
  .today{margin-top:12px;border:1px dashed var(--hair-strong);border-radius:12px;padding:11px 14px;font-size:12.5px;line-height:1.45;color:var(--silver);background:var(--lift)}
  .today b{display:block;font-family:var(--mono);font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;color:var(--dim);font-weight:400;margin-bottom:4px}
  .today q{quotes:none;color:var(--fg)}
  .redo{list-style:none;display:flex;flex-direction:column;gap:9px;margin-top:4px}
  .redo li{border:1px solid var(--hair);border-radius:12px;background:var(--lift);padding:11px 14px 11px 46px;position:relative;box-shadow:var(--card-shadow)}
  .redo li .ic{position:absolute;left:13px;top:12px;width:22px;height:22px;border-radius:7px;background:rgba(131,102,255,0.12);color:var(--violet);font-family:var(--mono);font-size:10.5px;display:flex;align-items:center;justify-content:center}
  .redo li b{display:block;font-family:var(--disp);font-weight:600;font-size:15px;letter-spacing:-0.01em}
  .redo li span{display:block;font-size:13px;line-height:1.45;color:var(--silver);margin-top:2px}

  /* conversation slide: DM thread mock */
  .dmmock{padding:18px 22px;background:var(--paper);border-right:1px solid var(--hair);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.9);display:flex;flex-direction:column}
  .dm-head{display:flex;align-items:center;gap:10px;padding-bottom:10px;border-bottom:1px solid rgba(0,0,0,0.08)}
  .dm-av{width:36px;height:36px;border-radius:50%;background:#e9e5df;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;color:#4b4b4b;flex:none}
  .dm-who b{display:block;font-size:13.5px;font-weight:600}
  .dm-who span{display:block;font-size:11.5px;color:rgba(0,0,0,0.6)}
  .dm-thread{display:flex;flex-direction:column;gap:9px;margin-top:12px}
  .dm{max-width:90%;padding:9px 13px 10px;border-radius:12px;font-size:13.5px;line-height:1.45;white-space:pre-line;background:#fff;border:1px solid rgba(0,0,0,0.08);align-self:flex-start;border-bottom-left-radius:4px}
  .dm.me{align-self:flex-end;background:#e6f0fa;border-color:transparent;border-bottom-left-radius:12px;border-bottom-right-radius:4px}
  .dm .who{display:block;font-size:10.5px;color:rgba(0,0,0,0.55);margin-bottom:3px;font-weight:600;letter-spacing:0.02em;white-space:normal}
  .dm-card{margin-top:8px;border:1px solid rgba(0,0,0,0.1);border-radius:8px;overflow:hidden;background:#fff;color:rgba(0,0,0,0.9);white-space:normal}
  .dm-card .im{height:50px;background:#0b0b0b;color:#fff;padding:8px 11px;font-family:var(--disp);font-weight:600;font-size:12.5px;line-height:1.2;display:flex;align-items:flex-end;position:relative}
  .dm-card .im::before{content:"";position:absolute;left:0;top:0;width:100%;height:4px;background:#58e0e0}
  .dm-card .t{padding:7px 11px 8px;font-size:11.5px;color:rgba(0,0,0,0.65);line-height:1.35}
  .dm-note{margin-top:auto;padding-top:10px;font-size:12px;color:var(--dim);line-height:1.4}
  .stg .k{font-size:9.5px}
  .stagepanel.seq{min-height:470px;overflow:visible}

  /* maths slide: fee model */
  .roi-grid.six{grid-template-columns:1fr 1fr 1fr}
  .roi-cell .cv.sm{font-size:22px}
  .feeline{display:flex;flex-wrap:wrap;gap:8px 10px;align-items:center;font-size:13px;color:var(--silver);border:1px solid var(--hair);border-radius:12px;background:var(--paper);padding:10px 14px}
  .feeline b{font-family:var(--disp);font-weight:600;font-size:15px;color:var(--fg);letter-spacing:-0.01em}
  .feeline i{font-style:normal;color:var(--dim)}

  /* investment slide: one package */
  .inv1{display:grid;grid-template-columns:1.32fr 0.68fr;gap:18px;margin-top:22px;align-items:stretch}
  .prices{display:flex;gap:22px;margin-top:8px;align-items:flex-start}
  .prices .big{margin-top:0;flex:0 1 auto}
  .prices .big small{display:block;font-family:var(--body);font-size:13px;letter-spacing:0;text-transform:none;color:rgba(244,244,243,0.72);margin:8px 0 0;font-weight:400;max-width:30ch;line-height:1.4}
  .prices .plus{font-family:var(--disp);font-weight:600;font-size:34px;color:rgba(244,244,243,0.5);margin-top:4px;flex:none}
  .rec .inc{margin-top:14px}
  .rec .why{margin-top:14px}
  .nocap{margin-top:12px;display:flex;gap:8px;flex-wrap:wrap}
  .nocap span{border:1px solid rgba(255,255,255,0.22);border-radius:999px;padding:6px 12px;font-size:12.5px;color:rgba(244,244,243,0.85)}
"""

CSS_END = '</style>'
body_open = SRC.split('</style>')[1].split('<header class="nav">')[0]  # "\n</head>\n<body>\n\n"

NAV = f"""<header class="nav">
  <span class="navmark" aria-label="Do It Digital"><span class="l k">d</span><span class="l">o</span><span class="sp"></span><span class="l k">i</span><span class="l">t</span><span class="sp"></span><span class="l k">d</span><span class="l">i</span><span class="l">g</span><span class="l">i</span><span class="l">t</span><span class="l">a</span><span class="l">l</span><span class="dot">.</span></span>
  <div class="nav-right">
    <span class="nav-for"><img class="wm" src="hypr-wordmark.png" alt="HYPR Digital Marketing"><span>For HYPR</span></span>
    <a class="nav-cta" data-cta href="#">Book the decision call</a>
  </div>
</header>
<div class="progress" id="progress"></div>

<div class="deck" id="deck">
"""

SLIDES = f"""
  <!-- 1 COVER -->
  <section class="slide glow center" data-title="Cover">
    <div class="wrap cover">
      <div class="lockup reveal"><div class="mk">did<span class="dot">.</span></div><span class="x">×</span><img class="wm" src="hypr-wordmark.png" alt="HYPR Digital Marketing"></div>
      <p class="eyebrow reveal">LinkedIn Outbound · Prepared for HYPR Digital Marketing</p>
      <h1 class="grad reveal">Discovery calls every week, not whenever the next referral&nbsp;lands<span class="stop">.</span></h1>
      <p class="lead reveal">LinkedIn outbound run in Pritpal's name, from a profile rebuilt around the e-com brands HYPR wants more of. We find the right founders, start the conversations, qualify the decision maker and book the call. Jay closes.</p>
      <div class="cover-bullets reveal"><span>Positioning and graphics rebuilt</span><span>Named target list</span><span>Warm and cold sequences</span><span>Calls booked into Jay's calendar</span><span>Small retainer, 50% of the first invoice</span></div>
      <p class="cover-meta reveal">Prepared for <b>Pritpal Bhachu, HYPR Digital Marketing</b><br>Prepared by <b>Nas Vou, Do It Digital</b> · {DATE}</p>
      <div class="hero-cta reveal"><button class="ghostbtn" data-goto="1">Read the proposal</button><button class="ghostbtn" data-goto="9">Go to the investment</button></div>
    </div>
  </section>

  <!-- 2 THE SITUATION -->
  <section class="slide ink" data-title="The situation">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">02</span>The situation</p>
      <h2 class="sec-head grad reveal">The close rate is not the problem. The number of discovery calls is<span class="stop">.</span></h2>
      <div class="diag">
        <div class="dlist reveal">
          <div class="dl"><span class="k">01</span><b>How HYPR wins work today</b><p>Referrals from your network and from clients you have delivered for. Warm and high-converting, and in your own words, not sustainable. They arrive when they arrive.</p></div>
          <div class="dl"><span class="k">02</span><b>What has been tried</b><p>Conferences in London, China, Dubai and Bucharest, at a cost you would rather have in the business now. Lead-gen agencies on retainer that produced one lead here and there. Both are being wound down.</p></div>
          <div class="dl"><span class="k">03</span><b>What is running now</b><p>Cold email brought in-house: lists bought, around thirty inboxes warmed, live for about a month and not yet compounding. Your own LinkedIn presence, building, with reach still low.</p></div>
          <div class="dl"><span class="k">04</span><b>What happens once someone is in the room</b><p>A free discovery call with a competitor breakdown and a roadmap. More than half sign. The bigger clients you have signed have stayed for one to two years.</p></div>
          <div class="dl"><span class="k">05</span><b>The actual constraint</b><p>Nobody owns the front of the funnel full time. Pritpal gets people in front of Jay in between running operations. The delivery side is built to scale five to ten times. The calendar is the bottleneck.</p></div>
        </div>
        <div class="reveal">
          <div class="prob">
            <div class="card"><div class="k">Where the calls come from today</div><h4>Warm and unpredictable</h4><p>Referrals, the network, the odd partner. Good months and quiet months, and no way to turn the tap.</p></div>
            <div class="card"><div class="k">Where the buyers already are</div><h4>On LinkedIn, by name</h4><p>Founders and owners of e-com brands at USD 1M to 5M are identifiable by title, sector and company size, and reachable for the price of a connection request. Most have never heard of HYPR.</p></div>
          </div>
          <div class="note" style="margin-top:14px"><b>What needs to happen</b> A profile that converts the click. A named list of the right accounts. Conversations started and followed up in Pritpal's voice every working day. Decision makers qualified and booked into Jay's calendar, with the pipeline visible to you every week.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 THE 12-WEEK OUTCOME -->
  <section class="slide" data-title="The 12-week outcome">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">03</span>The 12-week outcome</p>
      <h2 class="sec-head grad reveal">A booked-call system that runs whether or not a referral shows&nbsp;up<span class="stop">.</span></h2>
      <div class="outc">
        <div class="reveal">
          <div class="blocklbl">By week 12, you will have</div>
          <ol class="outs">
            <li><b>A positioned profile</b><span>Headline, about and featured rewritten around e-com brands that need organic visibility, with a new banner and featured cards in HYPR's brand.</span></li>
            <li><b>A named target list</b><span>E-com D2C founders and owners at USD 1M to 5M, the sweet spot you named. Then fitness, beauty and B2B brands. Decision makers only.</span></li>
            <li><b>Three sequences running</b><span>Warm, to people who engage or already sit in the network. Cold, to the list. Re-engagement, for everyone who went quiet. All in Pritpal's voice.</span></li>
            <li><b>Calls in Jay's calendar</b><span>Every booked call handed over in Slack with the thread, the brand, the decision maker and what they asked for.</span></li>
            <li><b>A weekly pipeline report</b><span>Requests, acceptances, replies, conversations and calls booked, plus your feedback on fit, so the targeting sharpens every week.</span></li>
            <li><b>An attribution ledger</b><span>Every signed client traced to the conversation or introduction that started it. That is what the 50% is calculated on.</span></li>
          </ol>
          <div class="note"><b>Honest line</b> We control the list, the messaging and the daily activity. We do not control who signs, and no number of calls or clients is promised.</div>
        </div>
        <div class="reveal">
          <div class="blocklbl">Real screens from our client portal and profile tool. Hover to enlarge</div>
          <div class="pgrid">
            <figure class="browser card zm zl zt"><img class="zoom" src="clients/profile-tool.png" alt="" aria-hidden="true"><div class="bbar"><i></i><i></i><i></i><span>profile.doitdigital.agency</span></div><img src="clients/profile-tool.png" alt="Free AI LinkedIn Profile Optimizer"><figcaption><b>Week one, the score.</b> Pritpal's profile scored before the rewrite, so the difference is measurable.</figcaption></figure>
            <figure class="browser card zm zr zt"><img class="zoom" src="shots/portal-profile.png" alt="" aria-hidden="true"><div class="bbar"><i></i><i></i><i></i><span>portal · profile rebuild</span></div><img src="shots/portal-profile.png" alt="Portal, profile rebuild with before and after"><figcaption><b>Week two, the rewrite.</b> Headline, about, banner and featured, approved section by section before anything goes live.</figcaption></figure>
            <figure class="browser card zm zl zb"><img class="zoom" src="shots/portal-reporting.png" alt="" aria-hidden="true"><div class="bbar"><i></i><i></i><i></i><span>portal · reporting</span></div><img src="shots/portal-reporting.png" alt="Portal, outbound performance reporting"><figcaption><b>Every week, the numbers.</b> Connection requests, acceptances, replies, meetings booked.</figcaption></figure>
            <figure class="browser card zm zr zb"><img class="zoom" src="clients/slack-win.webp" alt="" aria-hidden="true"><div class="bbar"><i></i><i></i><i></i><span>client slack · shared channel</span></div><img src="clients/slack-win.webp" alt="A client Slack channel reporting a win"><figcaption><b>Every call, in Slack.</b> A real client channel. Handovers, questions and wins live in one place.</figcaption></figure>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4 THE SYSTEM -->
  <section class="slide" data-title="The system">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">04</span>The system</p>
      <h2 class="sec-head grad reveal">Four layers. One job: the right founder in Jay's calendar<span class="stop">.</span></h2>
      <div class="col4">
        <div class="blk card reveal"><div class="k">Layer 1</div><h3>Positioning</h3><p>Every message we send leads to the profile. It has to convert the click.</p><ul class="v8list"><li>Headline, about and experience rewritten for the buyer</li><li>Banner and featured cards designed in HYPR's brand</li><li>Case studies turned into one-screen proof</li><li>Approved section by section in the portal</li></ul></div>
        <div class="blk card reveal"><div class="k">Layer 2</div><h3>The list</h3><p>Named accounts, decision makers only, built in Sales Navigator and checked by hand.</p><ul class="v8list"><li>E-com D2C at USD 1M to 5M revenue</li><li>Founder, owner, CEO and CMO titles</li><li>Fitness, beauty, wine, home and medical, then B2B brand awareness</li><li>Refreshed every cycle from your feedback on fit</li></ul></div>
        <div class="blk card reveal"><div class="k">Layer 3</div><h3>Sequences</h3><p>Warm first, then cold, all written in Pritpal's voice and approved before they run.</p><ul class="v8list"><li><strong>Warm.</strong> Engagers, profile viewers, the existing network, past conversations</li><li><strong>Cold.</strong> Connection request, opener, proof, ask</li><li>Never a pitch in message one</li><li>Connection requests at the account's limit</li></ul></div>
        <div class="blk card reveal"><div class="k">Layer 4</div><h3>Handover</h3><p>Qualified, then booked. Nothing lands in Jay's calendar that has not been checked.</p><ul class="v8list"><li>Inbox managed every working day</li><li>Decision maker on marketing spend confirmed</li><li>Call booked into Jay's calendar, Slack post with the thread</li><li>Weekly pipeline report and your feedback loop</li></ul><p><strong style="color:var(--fg)">Positioning earns the reply. Outbound goes and gets it.</strong></p></div>
      </div>
    </div>
  </section>

  <!-- 5 POSITIONING AND GRAPHICS -->
  <section class="slide" data-title="Positioning and graphics">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">05</span>Positioning and graphics</p>
      <h2 class="sec-head grad reveal">Before anyone replies, they look at the profile. We rebuild it around the buyer<span class="stop">.</span></h2>
      <div class="pos">
        <div class="reveal">
          <div class="prof card">
            <div class="banner"><div class="lg"><img src="hypr-wordmark.png" alt="HYPR"></div><div class="hl">Organic traffic that <i>stays</i> when the ads stop.</div><div class="sub">Content for e-com and consumer brands, published on 300+ sites.</div><div class="bstrip">Fitness · Beauty · Wine · Medical · B2B</div></div>
            <span class="tag">Mock-up · direction for week one</span>
            <div class="head"><div class="av">PB</div><div class="nm">Pritpal Bhachu <i>· 1st</i></div><div class="hd">Organic traffic for e-com brands doing USD 1M to 5M · Articles, video and podcasts published on 300+ sites · Traffic that stays when the ads stop · Director, HYPR Digital Marketing</div><div class="meta">London, United Kingdom · Contact info</div><div class="btns"><span class="p">Message</span><span>Book a discovery call</span></div></div>
            <div class="feat"><div class="fk">Featured</div><div class="fcards">
              <div class="fc"><div class="im">Fitness brand, 12 months</div><div class="cap">Blog from 221 to 50K visits a month. 23.5K new keywords.</div></div>
              <div class="fc"><div class="im c">What HYPR does, on one page</div><div class="cap">Find the topics, create every format, distribute to 300+ sites.</div></div>
              <div class="fc"><div class="im w">Book a discovery call</div><div class="cap">A competitor breakdown and a roadmap, free, with Jay.</div></div>
            </div></div>
          </div>
        </div>
        <div class="reveal">
          <div class="blocklbl">What we redo, and why</div>
          <ul class="redo">
            <li><span class="ic">01</span><b>Headline and about</b><span>Written for the buyer, not the industry. Who it is for, what changes for them, and the proof, in that order.</span></li>
            <li><span class="ic">02</span><b>Featured section</b><span>The case studies you already have, turned into 1200 by 627 cards people open. In your words, the PDFs are not getting read.</span></li>
            <li><span class="ic">03</span><b>Banner</b><span>1584 by 396, in HYPR's brand. One line that says what you do and for whom, with the 300-site distribution as the proof.</span></li>
            <li><span class="ic">04</span><b>Experience and services</b><span>Aligned to the same positioning so the whole profile reads as one story and one offer.</span></li>
            <li><span class="ic">05</span><b>Sign-off</b><span>Every section approved by Pritpal in the portal before it goes live. Nothing changes on the profile without a yes.</span></li>
          </ul>
          <div class="today"><b>The headline today</b><q>Driving Organic Traffic Growth for Brands | 61.5x ROI | 20,000% Traffic Growth | No Paid Ads | On and Off-Site Multi-Format Content + Distribution</q><br>Strong proof, but no buyer is named. An e-com founder has no reason to think it is about them.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 6 THE CONVERSATION -->
  <section class="slide" data-title="The conversation">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">06</span>The conversation</p>
      <h2 class="sec-head grad reveal">Five touches. Each one earns the next. No pitch in message&nbsp;one<span class="stop">.</span></h2>
      <p class="sec-lead reveal">In Pritpal's voice, approved before it runs. Click a touch to read it.</p>
      <div class="track reveal"><i></i><i></i><i></i><i></i><i></i></div>
      <div class="stages reveal" role="tablist">
        <button class="stg active" data-stage="0" role="tab"><span class="k">01 · Day 0</span><b>The request</b><small>A connection request to a named founder on the list</small><em>Job: get accepted by the right people</em></button>
        <button class="stg" data-stage="1" role="tab"><span class="k">02 · Day 1 to 2</span><b>The opener</b><small>One real observation about their brand, one easy question</small><em>Job: start a real conversation</em></button>
        <button class="stg" data-stage="2" role="tab"><span class="k">03 · Day 4 to 6</span><b>The proof</b><small>A client result they can read in ten seconds</small><em>Job: make the outcome concrete</em></button>
        <button class="stg" data-stage="3" role="tab"><span class="k">04 · Day 9 to 12</span><b>The ask</b><small>The free competitor breakdown Jay already runs</small><em>Job: book a qualified call</em></button>
        <button class="stg" data-stage="4" role="tab"><span class="k">05 · Day 20 on</span><b>Re-engagement</b><small>A new angle for everyone who went quiet</small><em>Job: keep the door open</em></button>
      </div>
      <div class="stagepanel seq card reveal">
        <div class="dmmock">
          <div class="dm-head"><div class="dm-av">D</div><div class="dm-who"><b>Dana</b><span>Founder, home fitness brand · example account</span></div></div>
          <div class="dm-thread" id="sq-thread"></div>
          <div class="dm-note">Example messages, written to show the shape. The live sequences are written with Pritpal in week two and approved before anything is sent.</div>
        </div>
        <div class="stageinfo">
          <div class="k" id="sq-k"></div>
          <h3 id="sq-title"></h3>
          <div class="si"><b>Format</b><p id="sq-fmt"></p></div>
          <div class="si"><b>Job</b><p id="sq-job"></p></div>
          <div class="si"><b>The ask</b><p id="sq-ask"></p></div>
          <div class="si"><b>Then</b><p id="sq-then"></p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- 7 PROOF -->
  <section class="slide" data-title="How we have helped others">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">07</span>How we have helped others</p>
      <h2 class="sec-head grad reveal oneline">Two clients, 66 meetings booked<span class="stop">.</span></h2>
      <p class="sec-lead reveal">Results from our outbound systems, shown so you can see how we work with clients. The first is Harry Phokou, who pointed you our way, in his own words, on video.</p>
      <div class="proof3 two">
        <div class="pc card reveal">
          <button class="vposter" type="button" data-yt="OMitGLVVAwU" aria-label="Play Harry Phokou's testimonial"><img src="clients/hivemind-poster.webp" alt="Harry Phokou, founder of Hivemind"><span class="vplay"><svg viewBox="0 0 24 24" fill="currentColor" width="26" height="26"><path d="M8 5.5v13l11-6.5z"/></svg></span></button>
          <div class="body"><div class="k">Same avatar · agency founder</div><h3>Hivemind Marketing, 120 days on LinkedIn</h3><p>A marketing agency founder with credibility and no consistent channel. Profile rebuilt, list built, conversations run every week.</p>
            <div class="metrics"><div class="metric"><div class="mv">37</div><div class="ml">Meetings booked</div></div><div class="metric"><div class="mv">4</div><div class="ml">Clients signed</div></div><div class="metric"><div class="mv">7K</div><div class="ml">MRR added</div></div></div></div>
        </div>
        <div class="pc card reveal">
          <div class="body"><div class="k">Receipts · recruitment founder</div><h3>29 meetings, two deals closed won, $60K in the CRM</h3><p>Ten years on referrals, no system. Profile rebuilt, ideal client defined, conversations run every week. The client's own Slack and CRM:</p>
            <div class="receipts" style="margin-top:12px"><img src="clients/slack-win.webp" alt="Client Slack: a candidate accepted an offer and a contract moved to signing"><img src="clients/crm-closed.webp" alt="Client CRM: two deals closed won"></div></div>
        </div>
      </div>
      <div class="qstrip reveal">
        <div class="qs"><img src="clients/matias-sanchez.jpeg" alt="">"Rebuilt everything: our profile, our messaging, and the entire outbound engine, and delivered a steady stream of qualified conversations."<b>Matias Sanchez Elsner, MD, DICO</b></div>
        <div class="qs"><img src="clients/alvin-narsey.webp" alt="">"A standout when it comes to LinkedIn outreach and client acquisition. Someone you want in your corner."<b>Alvin Narsey, Business Coach for Retailers</b></div>
        <div class="qs"><img src="clients/harry-phokou.png" alt="">"I didn't know how good I could have it. I've done outbound now, I can't go back."<b>Harry Phokou, Founder, Hivemind</b></div>
      </div>
    </div>
  </section>

  <!-- 8 THE 12-WEEK PLAN -->
  <section class="slide" data-title="The 12-week plan">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">08</span>The 12-week plan</p>
      <h2 class="sec-head grad reveal">Position first, then list, then volume<span class="stop">.</span></h2>
      <div class="timeline reveal">
        <div class="tk"><span style="--p:8%"></span><span style="--p:25%"></span><span style="--p:42%"></span><span style="--p:58%"></span><span style="--p:75%"></span><span style="--p:92%"></span></div>
        <div class="tcards">
          <div class="tc"><div class="k">Week 1</div><b>Install</b><ul><li>Strategy call</li><li>ICP and list criteria agreed</li><li>Profile scored and audited</li><li>Headline, about and featured drafted</li><li>Banner and cards briefed</li><li>Slack channel and calendar link set up</li></ul></div>
          <div class="tc"><div class="k">Week 2</div><b>Foundation</b><ul><li>Profile and graphics approved and live</li><li>Target list built and approved</li><li>Sequences written in Pritpal's voice</li><li>Warm list assembled from engagers and the network</li></ul></div>
          <div class="tc"><div class="k">Week 3</div><b>Live</b><ul><li>Connection requests begin at the account's limit</li><li>Warm sequences start</li><li>Inbox managed every working day</li><li>First replies handled</li></ul></div>
          <div class="tc"><div class="k">Week 4</div><b>Rhythm</b><ul><li>Cold sequences at full volume</li><li>First calls booked and handed over</li><li>First weekly report</li><li>Your feedback on fit, list refined</li></ul></div>
          <div class="tc m"><div class="k">Weeks 5 to 8</div><b>Iterate</b><ul><li>Messaging revised on reply data</li><li>Second segment: fitness, beauty, B2B brand awareness</li><li>Re-engagement sequence live</li><li>First attributed clients logged as Jay signs</li></ul></div>
          <div class="tc m"><div class="k">Weeks 9 to 12</div><b>Scale and decide</b><ul><li>Volume on what books</li><li>Playbook documented</li><li>Attribution ledger reconciled</li><li>Cycle-four decision</li></ul></div>
        </div>
      </div>
      <div class="decide dark reveal"><b>Week 12 · Decide</b><span>Keep the system running, add cold email on the inboxes you have already warmed, or add founder content so the outbound lands on a feed that is already talking to the buyer.</span></div>
    </div>
  </section>

  <!-- 9 THE MATHS -->
  <section class="slide" data-title="The maths">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">09</span>The maths</p>
      <h2 class="sec-head grad reveal">Your numbers, your maths<span class="stop">.</span></h2>
      <p class="sec-lead reveal">Put in what a client is worth to HYPR each month, how long they stay, how many discovery calls the outbound books in 12 weeks, and Jay's close rate. The retainer and the 50% fall out of that.</p>
      <div class="roi">
        <div class="roi-in card reveal">
          <div class="feeline"><b>GBP 1,100</b><i>every 28 days, three cycles</i><span>+</span><b>50% of the first invoice</b><i>per client signed, no cap</i></div>
          <div class="ctl">
            <label for="r-inst"><span>Average client value per month (USD)</span><output id="o-inst">USD 4,500</output></label>
            <input type="range" id="r-inst" min="1000" max="20000" step="250" value="4500">
          </div>
          <div class="ctl">
            <label for="r-len"><span>Average client stays</span><output id="o-len">12 months</output></label>
            <input type="range" id="r-len" min="3" max="36" step="1" value="12">
          </div>
          <div class="ctl">
            <label for="r-dem"><span>Discovery calls booked in 12 weeks</span><output id="o-dem">12</output></label>
            <input type="range" id="r-dem" min="0" max="40" step="1" value="12">
          </div>
          <div class="ctl">
            <label for="r-cr"><span>Close rate on a discovery call</span><output id="o-cr">40%</output></label>
            <input type="range" id="r-cr" min="10" max="80" step="5" value="40">
          </div>
        </div>
        <div class="roi-out card reveal">
          <div class="k" id="o-against">Against a 12-week retainer of GBP 3,300</div>
          <div class="hero">
            <div class="hv" id="o-mult">4x</div>
            <div class="hl" id="o-hero"></div>
          </div>
          <div class="roi-grid six">
            <div class="roi-cell"><div class="cv" id="o-cli">4.8</div><div class="cl">Clients expected</div></div>
            <div class="roi-cell"><div class="cv sm" id="o-cv">USD 259,200</div><div class="cl">Contract value</div></div>
            <div class="roi-cell"><div class="cv sm" id="o-kept">USD 244,000</div><div class="cl">Kept by HYPR</div></div>
            <div class="roi-cell"><div class="cv sm" id="o-fee">USD 10,800</div><div class="cl">Success fees to did.</div></div>
            <div class="roi-cell"><div class="cv sm" id="o-cpc">GBP 275</div><div class="cl">Retainer per call booked</div></div>
            <div class="roi-cell"><div class="cv sm" id="o-be">1 client, 2 months</div><div class="cl">Pays back everything</div></div>
          </div>
          <div class="foot" id="o-foot"></div>
        </div>
      </div>
      <details class="assump reveal">
        <summary><span class="k">Assumptions behind the numbers</span><span class="tog">Show</span></summary>
        <ul>
          <li><b>Retainer</b> GBP 1,100 every 28 days for three cycles, GBP 3,300 in total, counted here as USD 4,400 at an indicative 1.33. Tooling at cost, excluded.</li>
          <li><b>Success fee</b> 50% of the first invoice of every client attributed to a conversation we ran or an introduction we made, counted here as one month of the client's package.</li>
          <li><b>Client value and tenure</b> Your figures. You told us the sweet spot is USD 3,000 to 6,000 a month and the bigger clients have stayed one to two years. Value is monthly package times months stayed, gross.</li>
          <li><b>Calls and close rate</b> Discovery calls that start as a LinkedIn conversation we ran. You said more than half sign, so 40% is the conservative default.</li>
          <li><b>Not counted</b> Referrals from new clients, introductions from our network, or anything after the months entered. A planning estimate, not a forecast.</li>
        </ul>
      </details>
    </div>
  </section>

  <!-- 10 INVESTMENT -->
  <section class="slide ink" data-title="Investment and risk reversal">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">10</span>Investment and risk reversal</p>
      <h2 class="sec-head grad reveal oneline">One package. Billed every 28 days. Paid mostly when Jay signs<span class="stop">.</span></h2>
      <div class="inv1">
        <div class="rec card reveal">
          <div class="k">LinkedIn Outbound · positioned</div>
          <div class="prices">
            <div class="big">GBP 1,100<span>every 28 days</span><small>The retainer. Covers the people, the list and the daily work.</small></div>
            <div class="plus">+</div>
            <div class="big">50%<span>of the first invoice</span><small>Of every client you sign from a conversation we ran or an introduction we made.</small></div>
          </div>
          <div class="nocap"><span>No cap on the fee</span><span>No cap on the number of clients</span><span>No cap on the calls we book</span></div>
          <div class="tl2">Retainer paid in advance each cycle. Three cycles to start (12 weeks), then cycle to cycle with 28 days' notice. The 50% falls due when the client's first invoice is paid, on any client whose first contact we logged at handover.</div>
          <ul class="inc"><li>Headline, about and featured rewritten</li><li>Banner and featured cards, HYPR's brand</li><li>Named target list, decision makers only</li><li>Connection requests at the account limit</li><li>Warm sequences to engagers and viewers</li><li>Cold and re-engagement sequences</li><li>Inbox managed every working day</li><li>Qualified calls booked into Jay's calendar</li><li>Slack channel, weekly report, ledger</li><li>Sales Navigator and tooling at cost</li></ul>
          <div class="why"><b>Twelve weeks</b> positions the profile, runs the list through three full sequences and shows what books. The week-12 decision is made on data, not on a feeling.</div>
        </div>
        <div class="tcol reveal">
          <div class="bd"><b>Delivery</b>If we miss an agreed deliverable because of our team, we make it up at no additional cost. If approvals or inputs are delayed, the timeline moves accordingly.</div>
          <div class="bd"><b>Voice</b>If a message does not sound like Pritpal during the first cycle, we rewrite it until it does. Nothing is sent from a template he has not approved.</div>
          <div class="bd"><b>Assets</b>You own these from day one: the profile rewrite, the banner and card files, the target list, the sequences, the reports and the attribution ledger.</div>
          <div class="bd"><b>Measurement</b>We report the activity and pipeline signals we can observe. We do not claim revenue that cannot be attributed. There is no results guarantee, and both sides earn more only when Jay signs.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 11 NEXT STEPS -->
  <section class="slide glow center close" data-title="Next steps">
    <div class="wrap">
      <p class="eyebrow reveal"><span class="n">11</span>Next steps</p>
      <h2 class="reveal">Decide whether the front of your funnel gets an owner for the next 12 weeks<span class="stop">.</span></h2>
      <div class="closegrid">
        <div class="cg card reveal"><div class="k">On the decision call</div><h3>We will</h3><ol><li>Confirm the ideal client and the first list segment</li><li>Agree the positioning direction and the headline</li><li>Replace the planning assumptions with your numbers</li><li>Agree how attribution is logged and when the 50% falls due</li><li>Set up the Slack channel and the calendar link</li><li>Confirm Pritpal's approval process for messages</li><li>Answer the commercial and operational questions</li></ol></div>
        <div class="cg card reveal"><div class="k">After a yes</div><h3>The first four weeks</h3><ol><li>Strategy call within seven days</li><li>Profile and graphics drafted in week one, live by week two</li><li>List and sequences approved in week two</li><li>Connection requests and warm sequences from week three</li><li>First weekly pipeline report at the end of week four</li></ol></div>
      </div>
      <p class="the-decision reveal"><b>The decision.</b> You have the case studies, the close rate and the capacity to scale. The question is whether the front of the funnel keeps depending on who Pritpal already knows, or gets a system that runs every working day and is paid mostly when Jay signs.</p>
      <div class="reveal" style="display:flex;justify-content:center;margin-top:24px"><a class="pillbtn" data-cta href="#">Book the decision call</a></div>
      <div class="closebar reveal"><div class="mk">did<span class="dot">.</span></div><div class="links"><a data-cta href="#">Book the decision call</a><a href="mailto:admin@doitdigital.agency">admin@doitdigital.agency</a><span class="muted">doitdigital.agency</span></div></div>
      <p class="fine reveal">LinkedIn Outbound · Prepared for Pritpal Bhachu, HYPR Digital Marketing · Prepared by Do It Digital · {DATE} · © 2026 Do It Digital.</p>
    </div>
  </section>
</div>

<div class="controls">
  <button class="ctrl-btn" id="prevBtn" aria-label="Previous"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg></button>
  <div class="counter" id="counter">1 / 11</div>
  <button class="ctrl-btn" id="nextBtn" aria-label="Next"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg></button>
</div>
<div class="kb-hint"><kbd>&larr;</kbd><kbd>&rarr;</kbd> navigate · <kbd>F</kbd> fullscreen</div>
"""

SCRIPT = r"""
<script>
  const CTA_HREF = 'https://calendly.com/do-it-digital';
  document.querySelectorAll('[data-cta]').forEach(a => a.setAttribute('href', CTA_HREF));

  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('counter');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const progress = document.getElementById('progress');
  let current = 0;

  slides.forEach(s => s.querySelectorAll('.reveal').forEach((el, i) => el.style.setProperty('--rd', (i * 70) + 'ms')));

  function show(i){
    current = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach((s, idx) => s.classList.toggle('active', idx === current));
    counter.textContent = `${current + 1} / ${slides.length}`;
    progress.style.width = `${((current + 1) / slides.length) * 100}%`;
    prevBtn.disabled = current === 0;
    nextBtn.disabled = current === slides.length - 1;
    slides[current].scrollTop = 0;
    tracker.onSlide(current);
  }
  const next = () => show(current + 1);
  const prev = () => show(current - 1);

  prevBtn.addEventListener('click', prev);
  nextBtn.addEventListener('click', next);
  document.querySelectorAll('[data-goto]').forEach(b => b.addEventListener('click', () => show(parseInt(b.dataset.goto, 10))));
  document.addEventListener('keydown', e => {
    if(e.target && e.target.tagName === 'INPUT') return; /* let the sliders own the arrow keys */
    if(e.key === 'ArrowRight' || e.key === ' '){ e.preventDefault(); next(); }
    if(e.key === 'ArrowLeft'){ e.preventDefault(); prev(); }
    if(e.key === 'f' || e.key === 'F'){ document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen(); }
  });
  let tsx = 0, tsTarget = null;
  document.addEventListener('touchstart', e => { tsx = e.touches[0].clientX; tsTarget = e.target; }, {passive:true});
  document.addEventListener('touchend', e => {
    if(tsTarget && tsTarget.tagName === 'INPUT') return;
    const dx = e.changedTouches[0].clientX - tsx;
    if(dx > 50) prev();
    if(dx < -50) next();
  });

  /* Fit: the deck is laid out at 1920x1080 and scaled to the window. Below 900px wide it falls back to the responsive layout. */
  const QA = new URLSearchParams(location.search).get('qa') === '1';
  (() => {
    const deck = document.getElementById('deck');
    const fit = () => {
      if(QA){ document.body.classList.add('staged'); deck.style.setProperty('--z', 1); return; }
      const w = window.innerWidth, h = window.innerHeight, on = w >= 900;
      document.body.classList.toggle('staged', on);
      if (on) deck.style.setProperty('--z', Math.min(w / 1920, h / 1080)); else deck.style.removeProperty('--z');
    };
    fit(); window.addEventListener('resize', fit);
  })();

  /* The conversation: five touches drive the DM thread mock */
  (() => {
    const me = (t, card) => ({ who: 'Pritpal', me: true, t, card });
    const them = t => ({ who: 'Dana', me: false, t });
    const CARD = '<div class="dm-card"><div class="im">Fitness brand, 12 months</div><div class="t">Blog from 221 to 50K visits a month. 23.5K new keywords. A fraction of the ad budget.</div></div>';
    const stages = [
      { k: '01 · Day 0 · The request', title: 'A connection request to a named founder on the list',
        thread: [ me('Hi Dana, your range came up while I was looking at how home-fitness brands rank against Peloton and NordicTrack. I work on organic traffic for e-com brands. Good to connect.') ],
        fmt: 'A short note, or no note at all. We test both and keep whichever gets the higher acceptance rate from the right people.', job: 'Get accepted by the founders and owners on the list, at the account\'s daily limit.', ask: 'None.', then: 'Accepted: the opener goes out within two days. Not accepted: they wait for the next cycle.' },
      { k: '02 · Day 1 to 2 · The opener', title: 'One real observation about their brand, one easy question',
        thread: [ me('Thanks for connecting, Dana. Quick one, no pitch. I had a look at the site before sending the request: strong on paid, and the blog has a dozen posts that do not rank for anything a buyer would type. That is usually the cheapest traffic a brand your size is leaving on the table.\n\nRoughly how much of your traffic is paid at the moment?'), them('Most of it, honestly. Organic is maybe 15%.') ],
        fmt: 'One message. Something we actually looked at, then a question they can answer in one line.', job: 'Start a conversation about their situation, not ours.', ask: 'A one-line answer.', then: 'A reply moves them to the proof. Silence moves them to re-engagement in three weeks.' },
      { k: '03 · Day 4 to 6 · The proof', title: 'A client result they can read in ten seconds',
        thread: [ me('That is where most brands your size sit. One of our fitness clients was there 12 months ago: the blog did 221 visits a month. It now does 50K a month and ranks for 23,500 search terms it never ranked for before, on a fraction of the ad spend. The short version is below.', CARD) ],
        fmt: 'The featured card from the profile, dropped into the thread. Real numbers from a real client, never a deck.', job: 'Make the outcome concrete before anyone asks for anything.', ask: 'None yet. Let them read.', then: 'Any reaction, even a like, moves them to the ask.' },
      { k: '04 · Day 9 to 12 · The ask', title: 'The free competitor breakdown Jay already runs',
        thread: [ me('Dana, would it be useful if we ran a competitor breakdown for your brand? Jay does these on a 45-minute call: where Peloton and NordicTrack take their traffic from, what you could realistically take back, and a roadmap. No charge and no obligation.\n\nAre you the right person for marketing spend, or should someone else join?'), them('Yes, that would be useful. It is me and my co-founder. Send me some times.'), me('Great. Here is Jay\'s calendar. I will send a short note beforehand so nothing on the call is wasted.') ],
        fmt: 'The discovery call you already give away, framed as the breakdown it is. The decision maker is confirmed before anything is booked.', job: 'Book a qualified call.', ask: 'A time in Jay\'s calendar.', then: 'Booked: a Slack post with the thread, the brand, the decision maker and what they asked for. Jay walks in briefed.' },
      { k: '05 · Day 20 onwards · Re-engagement', title: 'A new angle for everyone who went quiet',
        thread: [ me('Dana, one thing that may be relevant. Since Google started de-indexing AI-written content, three of the brands that came to us had lost around 60% of their organic traffic. Human-edited content is what survives it.\n\nIf organic is on the list for next quarter, happy to send over what we would look at first.') ],
        fmt: 'A different angle every three to four weeks for people who did not reply. Never the same message twice.', job: 'Keep the door open without pestering.', ask: 'A soft one. Then they rest until the next cycle.', then: 'Every reply, whenever it comes, is handled the same day and logged in the weekly report.' },
    ];
    const btns = document.querySelectorAll('.stg');
    const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
    const set = i => {
      const st = stages[i];
      btns.forEach((b, j) => b.classList.toggle('active', j === i));
      document.getElementById('sq-k').textContent = st.k;
      document.getElementById('sq-title').textContent = st.title;
      document.getElementById('sq-fmt').textContent = st.fmt;
      document.getElementById('sq-job').textContent = st.job;
      document.getElementById('sq-ask').textContent = st.ask;
      document.getElementById('sq-then').textContent = st.then;
      document.getElementById('sq-thread').innerHTML = st.thread.map(m => `<div class="dm${m.me ? ' me' : ''}"><span class="who">${m.who}</span>${esc(m.t)}${m.card || ''}</div>`).join('');
    };
    btns.forEach(b => b.addEventListener('click', () => set(+b.dataset.stage)));
    set(0);
  })();

  /* The maths: retainer plus 50% of the first invoice, from the prospect's own inputs */
  (() => {
    const RET_GBP = __RET_GBP_TOTAL__, RET_USD = __RET_USD_TOTAL__;
    const $ = id => document.getElementById(id);
    const val = $('r-inst'), len = $('r-len'), dem = $('r-dem'), cr = $('r-cr');
    if(!val) return;
    const usd = n => 'USD ' + Math.round(n).toLocaleString('en-US');
    const gbp = n => 'GBP ' + Math.round(n).toLocaleString('en-US');
    const paint = el => el.style.setProperty('--pct', ((el.value - el.min) / (el.max - el.min) * 100) + '%');
    const words = ['No', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen'];
    const one = n => n.toFixed(1).replace(/\.0$/, '');
    function calc(){
      const v = +val.value, m = +len.value, calls = +dem.value, rate = +cr.value / 100;
      const c = calls * rate, cv = v * m * c, fee = 0.5 * v * c, paid = RET_USD + fee, kept = cv - fee;
      const mult = paid > 0 ? cv / paid : 0;
      const beMonths = Math.ceil(RET_USD / v + 0.5);
      $('o-inst').textContent = usd(v);
      $('o-len').textContent = m + (m === 1 ? ' month' : ' months');
      $('o-dem').textContent = calls;
      $('o-cr').textContent = Math.round(rate * 100) + '%';
      $('o-against').textContent = 'Against a 12-week retainer of ' + gbp(RET_GBP) + ', about ' + usd(RET_USD);
      $('o-cli').textContent = one(c);
      $('o-mult').textContent = c === 0 ? '0x' : (mult >= 10 ? Math.round(mult) : mult.toFixed(1).replace(/\.0$/, '')) + 'x';
      $('o-cv').textContent = usd(cv);
      $('o-kept').textContent = usd(Math.max(0, kept));
      $('o-fee').textContent = usd(fee);
      $('o-cpc').textContent = calls === 0 ? 'n/a' : gbp(RET_GBP / calls);
      $('o-be').textContent = beMonths <= m ? '1 client, ' + beMonths + (beMonths === 1 ? ' month' : ' months') : Math.ceil(RET_USD / (v * Math.max(0.5, m - 0.5))) + ' clients';
      $('o-hero').textContent = calls === 0
        ? 'With no calls booked the system has cost ' + gbp(RET_GBP) + ' and nothing else is owed. One client at ' + usd(v) + ' a month covers it in ' + beMonths + (beMonths === 1 ? ' month.' : ' months.')
        : (calls <= 15 ? words[calls] : calls) + (calls === 1 ? ' call' : ' calls') + ' at a ' + Math.round(rate * 100) + '% close is about ' + one(c) + (c === 1 ? ' client' : ' clients') + '. At ' + usd(v) + ' a month for ' + m + ' months, that is ' + usd(cv) + ' in contract value. You pay us ' + usd(paid) + ' in total, ' + usd(fee) + ' of it only after Jay signs.';
      $('o-foot').textContent = 'Contract value divided by everything paid to us, retainer and success fees together. ' + (beMonths <= m
        ? 'One client staying ' + beMonths + (beMonths === 1 ? ' month' : ' months') + ' covers the retainer and its own fee. Everything after that is return.'
        : 'Break-even needs more than one client at this value and tenure.');
      [val, len, dem, cr].forEach(paint);
    }
    [val, len, dem, cr].forEach(el => el.addEventListener('input', calc));
    calc();
  })();

  /* Video testimonial: poster first, YouTube loads on click */
  document.querySelectorAll('.vposter').forEach(b => b.addEventListener('click', () => {
    const f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0';
    f.title = b.getAttribute('aria-label'); f.allow = 'autoplay; fullscreen; picture-in-picture'; f.allowFullscreen = true;
    b.replaceWith(f);
  }));

  /* View tracking: the shared Do It Digital Apps Script collector. Tag the share link with ?v=<first name>. */
  const TRACKING = { endpoint: 'https://script.google.com/macros/s/AKfycbwA7cVeaqvuVkfGPIAf9GeA_YriMInYIM_QSsxtV1Q8r140_wsIFidMBsLhUQFhMHvV3g/exec', proposalId: 'hypr-outbound-v1', heartbeatSec: 20, debug: false };
  const tracker = (() => {
    const now = () => Date.now();
    const id = (k, store) => { try { let v = store.getItem(k); if(!v){ v = Math.random().toString(36).slice(2,10) + now().toString(36); store.setItem(k,v);} return v; } catch(e){ return 'na'; } };
    const vid = id('did_vid', localStorage), sid = id('did_sid', sessionStorage);
    const recipient = new URLSearchParams(location.search).get('v') || '';
    const titles = [...slides].map(s => s.dataset.title || '');
    const slideMs = new Array(slides.length).fill(0);
    let cur = 0, maxS = 0, enteredAt = now(), visible = !document.hidden, exitSent = false;
    const settle = () => { if(visible) slideMs[cur] += now() - enteredAt; enteredAt = now(); };
    const totalSec = () => Math.round(slideMs.reduce((a,b)=>a+b,0)/1000);
    function send(type, data){
      if(QA) return;
      const payload = Object.assign({ p: TRACKING.proposalId, t: type, ts: new Date().toISOString(), vid, sid, r: recipient, slide: cur+1, title: titles[cur] }, data||{});
      if(TRACKING.debug) console.log('[track]', payload);
      if(!TRACKING.endpoint) return;
      try { const body = JSON.stringify(payload);
        if(navigator.sendBeacon) navigator.sendBeacon(TRACKING.endpoint, new Blob([body], {type:'text/plain'}));
        else fetch(TRACKING.endpoint, {method:'POST', body, keepalive:true, mode:'no-cors'});
      } catch(e){}
    }
    function onSlide(i){ if(i !== cur){ settle(); send('slide_leave', { secOnSlide: Math.round(slideMs[cur]/1000) }); } cur = i; maxS = Math.max(maxS, i); enteredAt = now(); send('slide_view', {}); }
    function exit(reason){ if(exitSent) return; exitSent = true; settle(); send('exit', { reason, exitSlide: cur+1, exitTitle: titles[cur], maxSlide: maxS+1, totalSec: totalSec(), perSlideSec: slideMs.map(ms=>Math.round(ms/1000)).join('|') }); }
    document.addEventListener('visibilitychange', () => { if(document.hidden){ settle(); visible = false; exit('hidden'); } else { visible = true; enteredAt = now(); exitSent = false; send('return', {}); } });
    window.addEventListener('pagehide', () => exit('pagehide'));
    setInterval(() => { if(visible){ settle(); send('ping', { totalSec: totalSec() }); } }, TRACKING.heartbeatSec * 1000);
    document.querySelectorAll('[data-cta], .pillbtn, .ghostbtn').forEach(a => a.addEventListener('click', () => send('cta_click', { label: a.textContent.trim(), href: a.getAttribute('href') || '' })));
    /* ROI slider use is a strong buying signal, log it once per slider */
    document.querySelectorAll('.roi input').forEach(el => el.addEventListener('change', () => send('roi_adjust', { input: el.id, value: el.value }), { once: true }));
    send('open', { ref: document.referrer || '', ua: navigator.userAgent, vw: innerWidth, vh: innerHeight, lang: navigator.language });
    return { onSlide, send };
  })();

  /* Start slide (?s=N, for review and QA renders) */
  (() => {
    const q = new URLSearchParams(location.search);
    const s = parseInt(q.get('s') || '1', 10) || 1;
    if(QA) document.documentElement.classList.add('qa');
    show(Math.max(1, Math.min(slides.length, s)) - 1);
    if(QA){
      const badge = document.createElement('div');
      badge.style.cssText = 'position:fixed;left:8px;top:70px;z-index:999;font:12px monospace;background:#ff0;color:#000;padding:4px 8px;border-radius:4px';
      document.body.appendChild(badge);
      const report = () => { const sl = slides[current]; const t = 'QA slide ' + (current + 1) + ' ' + sl.dataset.title + ' overflowY=' + (sl.scrollHeight - sl.clientHeight) + ' overflowX=' + (sl.scrollWidth - sl.clientWidth); document.title = t; badge.textContent = t; };
      report();
      (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => setTimeout(report, 400));
    }
  })();
</script>
</body>
</html>
"""
SCRIPT = SCRIPT.replace('__RET_GBP_TOTAL__', str(RET_GBP_TOTAL)).replace('__RET_USD_TOTAL__', str(RET_USD_TOTAL))

html = head + EXTRA_CSS + CSS_END + body_open + NAV + SLIDES + SCRIPT
# House rules: no em or en dashes anywhere in our copy
assert '—' not in html and '–' not in html, 'dash found'
OUT.write_text(html, encoding='utf-8')
print('wrote', OUT, len(html), 'bytes;', html.count('<section class="slide'), 'slides')
