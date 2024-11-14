# Bluesky Starter Pack sync

[![Run Sync Script](https://github.com/jaseemabid/bluesky-sync/actions/workflows/sync.yaml/badge.svg)](https://github.com/jaseemabid/bluesky-sync/actions/workflows/sync.yaml)

🔄 Sync a list of users in [accounts.txt] to a Bluesky [starter pack][sp] and [list].

🐙 Add yourself to [accounts.txt] and send me a PR. Github actions will update the list after merge to main.

## Dev

1. Create `.env` file with `AT_LOGIN`, `AT_PASSWORD`, `STARTER_PACK_URI` and `LIST_URI`
2. `$ uv run --env-file .env sync.py`




[sp]: https://bsky.app/starter-pack/jabid.in/3lagxhtghxi2e
[accounts.txt]: https://github.com/jaseemabid/bluesky-sync/blob/main/accounts.txt
[list]: https://bsky.app/profile/jabid.in/lists/3lawghh5a6v2c

