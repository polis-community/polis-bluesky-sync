# Bluesky Starter Pack sync

[![Run Sync Script][workflow-badge]][workflow-link]

🔄 Sync a list of users in [accounts.txt] to a Bluesky [starter pack][sp] and [list].

🐙 Add yourself to [accounts.txt] and send me a PR. Github actions will update the list after merge to main.

## Dev

**Requirements:**
- [Install][uv-install] `uv` Python package manager

1. `$ cp sample.env .env` and supply your own values
2. `$ uv run --env-file .env sync.py`




[workflow-badge]: https://github.com/jaseemabid/bluesky-sync/actions/workflows/sync.yaml/badge.svg
[workflow-link]: https://github.com/jaseemabid/bluesky-sync/actions/workflows/sync.yaml
[accounts.txt]: /accounts.txt
[sp]: https://bsky.app/starter-pack/jabid.in/3lagxhtghxi2e
[list]: https://bsky.app/profile/jabid.in/lists/3lawghh5a6v2c
[uv-install]: https://docs.astral.sh/uv/getting-started/installation/

