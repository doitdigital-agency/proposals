# Do It Digital proposals

Interactive client proposal decks, one folder per client. Each deck is a self-contained index.html
with a noindex meta tag.

## Hosting

Decks are served at https://proposals.doitdigital.agency/<client-folder>/ by the Cloudflare Worker in
_worker/ (static assets plus a per-deck password gate; passwords live in the PASSWORDS secret, decks not
listed there are open). This GitHub repo stays the source of truth: push here, then run
_tools/deploy-proposals.sh to sync a fresh clone into the Worker and deploy. The old
doitdigital-agency.github.io/proposals/ links redirect to the new host via the CNAME file.

## Tracking

Tag every shared link with ?v=<name> so the built-in tracker shows who viewed. The tag survives the
password unlock redirect.
