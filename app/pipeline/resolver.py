def resolve_identities(full_name: str, location: str | None):
    # MVP: hardcode mocked accounts.
    # In real case: fuzzy match nama vs username publik, lokasi, dsb.
    accounts = [
        {
            "platform": "twitter",
            "handle": "@{}".format(full_name.lower().replace(" ", "")),
            "confidence": 0.82
        },
        {
            "platform": "linkedin",
            "handle": full_name + " | Civil Service Enthusiast",
            "confidence": 0.74
        }
    ]
    return accounts
