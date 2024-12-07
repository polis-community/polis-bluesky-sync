# Bluesky Starter Pack sync

[![Run Sync Script][workflow-badge]][workflow-link]

🔄 Sync a list of users in [accounts.txt] to a Bluesky [starter pack][sp] and [list].

🐙 Add yourself to [accounts.txt] and send me a PR. Github actions will update the list after merge to main.

## Dev

**Requirements:**
- [Install][uv-install] `uv` Python package manager

1. `$ cp sample.env .env` and supply your own values
2. `$ uv run --env-file .env sync.py`




[workflow-badge]: https://github.com/polis-community/polis-bluesky-sync/actions/workflows/sync.yaml/badge.svg
[workflow-link]: https://github.com/polis-community/polis-bluesky-sync/actions/workflows/sync.yaml
[accounts.txt]: /accounts.polis.txt
[sp]: https://bsky.app/starter-pack/patcon.bsky.social/3laxcisdajc2n
[list]: https://bsky.app/profile/patcon.bsky.social/lists/3lcqrsp3juf2b
[uv-install]: https://docs.astral.sh/uv/getting-started/installation/
