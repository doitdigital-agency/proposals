#!/usr/bin/env bash
# Deploy the proposal decks to proposals.doitdigital.agency (Cloudflare Worker with static assets + password gate).
# Source of truth stays the GitHub repo doitdigital-agency/proposals; this syncs a fresh clone into the Worker's assets.
# Usage: _tools/deploy-proposals.sh            (clones the repo, syncs, deploys)
#        _tools/deploy-proposals.sh --local    (syncs the local working folder instead of the repo)
set -euo pipefail
ROOT="/Users/Nas/Proposal Do It Digital"
WORKER="$ROOT/_worker"
SRC="/tmp/proposals-live"
if [[ "${1:-}" == "--local" ]]; then
  SRC="$ROOT"
else
  rm -rf "$SRC"
  git clone -q https://github.com/doitdigital-agency/proposals "$SRC"
fi
mkdir -p "$WORKER/site"
rsync -a --delete \
  --exclude '.git' --exclude '.github' --exclude '_*' --exclude '*.md' --exclude '.DS_Store' \
  --exclude 'tracking' --exclude 'Testimonials' --exclude 'Code.gs' --exclude '*.zip' --exclude 'team.html' \
  --exclude 'index.html' \
  "$SRC/" "$WORKER/site/"
# the root index.html of the repo is the old template; decks live in folders, so re-add each folder's index.html
rsync -a --include '*/' --include '*/index.html' --exclude '*' "$SRC/" "$WORKER/site/"
cd "$WORKER"
npx --yes wrangler deploy
echo "Deployed. Protected decks are listed in the PASSWORDS secret (wrangler secret put PASSWORDS)."
