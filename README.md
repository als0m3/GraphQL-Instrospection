# GraphQL Introspection CLI

Inspect the queries, arguments, and types exposed by a GraphQL endpoint.

## Setup

Use Python 3.10 or newer. From the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python GraphQL.py --help
.venv/bin/python GraphQL.py --url https://example.com/graphql
```

The endpoint must allow introspection. Run only against an endpoint you own or are authorized to inspect. An optional `--token` argument supplies a bearer token; avoid putting sensitive tokens into shell history or shared logs.

## Scope and limitations

This is an earlier CLI experiment. It displays queries and schema types; it is not a full GraphQL client. Authentication, disabled introspection, and unexpected response shapes may require adaptation. Run it from this directory because it reads `request.graphql` using a relative path.

Dependencies are limited to the HTTP client, terminal colors, and their transitive dependencies. To update the lock file, use `uv pip compile requirements.in --upgrade --generate-hashes -o requirements.txt`.

See [SECURITY.md](SECURITY.md) for private vulnerability reports.
