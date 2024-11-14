from atproto import Client, models
import os
from datetime import datetime
from datetime import timezone


def main():
    # Setup these 3 variables in a `.env` file or shell env
    STARTER_PACK_URI = os.environ["STARTER_PACK_URI"]
    LOGIN = os.environ["AT_LOGIN"]
    PASSWORD = os.environ["AT_PASSWORD"]

    with open("accounts.txt") as f:
        expected = set(line.strip() for line in f.readlines() if line.strip())

    client = Client()
    profile = client.login(LOGIN, PASSWORD)

    print(f"logged in as {profile.display_name}")

    # List of members in the starter pack
    members = client.app.bsky.graph.get_list({"list": STARTER_PACK_URI, "limit": 100})

    print(f"Found {members.list.list_item_count} users, expected {len(expected)}")

    # 🔥 TODO: Paginate this, get users after first 100
    found = set(m.subject.handle for m in members.items)

    # Step 1: Log extra users
    extra = found - expected
    if extra:
        print(f"Found {len(extra)} unexpected users, moving on it: {(extra)}")

    # Step 2: Add missing users
    missing = expected - found
    if not missing:
        print("No new users to add, exiting")
        return

    print(f"Adding {len(missing)} users to the starter pack: {list(missing)}")

    # ✨ Neat API to get all the missing users in one request
    profiles = client.app.bsky.actor.get_profiles({"actors": list(missing)})
    # ✨ All new users are added to the list in a single API
    writes = [
        models.ComAtprotoRepoApplyWrites.Create(
            collection="app.bsky.graph.listitem",
            value={
                "$type": "app.bsky.graph.listitem",
                "subject": p["did"],
                "list": STARTER_PACK_URI,
                "createdAt": datetime.now(timezone.utc).isoformat(),
            },
        )
        for p in profiles.profiles
    ]

    data = models.ComAtprotoRepoApplyWrites.Data(repo="jabid.in", writes=writes)

    print("Sending request")
    print(data.model_dump())

    resp = client.com.atproto.repo.apply_writes(data)

    print("Got response")
    print(resp)


if __name__ == "__main__":
    main()
