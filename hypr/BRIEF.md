# LinkedIn Outbound for HYPR Digital Marketing (2026-09-24)

## Purpose
Client proposal for Pritpal Bhachu (Director, HYPR Digital Marketing, London), following the 18 Sep 2026 call (Fathom 184439330, https://fathom.video/calls/827278980). Outbound only, no content package. Nas's brief: "a proposal just for my LinkedIn outbound. 1,100 pounds and a 50% referral fee of the first invoice. Nothing is capped here. Keep our standard LinkedIn Outbound + we would redo his LinkedIn positioning and graphics for him." Built from the generic Voice System deck (`voice-system/`), HYPR branding added from hyprdigitalmarketing.com (black serif wordmark, cyan #58e0e0 bar).

## Offer as the deck shows it
- **Retainer** GBP 1,100 every 28 days, paid in advance. Three cycles to start (12 weeks), then cycle to cycle with 28 days' notice.
- **Success fee** 50% of the first invoice of every client HYPR signs from a conversation we ran or an introduction we made. Due when the client's first invoice is paid. Attribution = first contact logged in the weekly report at handover. No cap on the fee, the number of clients or the calls booked.
- **Scope** headline, about, featured and experience rewritten; banner (1584x396) and featured cards (1200x627) in HYPR's brand; named target list (e-com D2C USD 1M to 5M, then fitness, beauty, B2B brand awareness; decision makers only); connection requests at the account limit; warm, cold and re-engagement sequences in Pritpal's voice; inbox managed every working day; qualified calls booked into Jay's calendar; Slack channel, weekly pipeline report, attribution ledger; Sales Navigator and tooling at cost.
- Process promises only (delivery, voice, assets, measurement). No results guarantee.

## Grounding (all from the call)
Referrals "not sustainable"; conferences (London worked, China, Dubai, Bucharest cost too much); lead-gen agencies on retainer produced "one lead here and there", being shut down; cold email brought in-house, ~30 inboxes warmed, about a month old; LinkedIn presence building, reach low; discovery calls free with a competitor breakdown, "over 50%" close; ~15 big clients, none left in 1 to 2 years; built to scale 5 to 10x; sweet spot USD 3k to 6k a month, some at 20k; success = 1 to 2 clients a month; Nas: 6 to 10 meetings a month; Pritpal proposed the small retainer + 50% of the first invoice; Jay closes, Pritpal gets people in front of him; Harry Phokou referred Pritpal. The "$250k loss" in the Fathom summary is NOT in the transcript, so it is not in the deck.
HYPR case study numbers (fitness brand, from the PDF Pritpal sent): blog 221 to 50K monthly visits, 23.5K new keywords, 200x blog traffic. Pritpal's current headline quoted verbatim from LinkedIn (via Kondo).

## Slides (11)
1 Cover · 2 The situation (ink) · 3 The 12-week outcome · 4 The system (four layers) · 5 Positioning and graphics (profile mock-up with HYPR-brand banner and featured cards, current headline quoted) · 6 The conversation (interactive five-touch DM sequence, example account "Dana") · 7 How we have helped others (verbatim from the generic deck; Harry first because he referred Pritpal) · 8 The 12-week plan · 9 The maths (retainer + 50% model; inputs client value USD, tenure, calls in 12 weeks, close rate; retainer counted as USD 4,400 at an indicative 1.33) · 10 Investment and risk reversal (ink) · 11 Next steps.

## Where
- Folder `hypr/`, tracker proposalId `hypr-outbound-v1`, share link `?v=pritpal`.
- Live: https://doitdigital-agency.github.io/proposals/hypr/?v=pritpal
- Local preview: launch config `hypr` on :8797.
- Build script: `_tools/build-hypr.py` (reads `voice-system/index.html` for the CSS, writes this folder's index.html; rebuild overwrites index.html only). Render/QA harness: `_tools/render.py` (writes to the scratchpad renders folder; change `out` if needed) (Chrome here writes its output and never exits, so the harness polls and kills it; `?s=N&qa=1` shows an overflow badge).

## QA (2026-09-24)
All 11 slides rendered at 1920x1080 with zero overflow after: outcome list tightened and image heights 172px; investment prices side by side at 48px; sector strip in the mock banner renamed `.bstrip` (a `.strip` rule already existed); conversation panel min-height 470px; footer text changed from "The Voice System" to "LinkedIn Outbound".

## Open with Nas
- Retainer read as every 28 days (house billing); confirm if he meant calendar months.
- The 50% is stated as "one month of the client's package" in the maths assumptions; confirm that is how HYPR defines "first invoice".
- Draft headline and banner line on slide 5 are a direction, to be agreed in week one.
