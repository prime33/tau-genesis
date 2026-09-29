#!/usr/bin/env python3
"""Schema validation on write (F6). validate(kind, obj) raises on a malformed record; every writer calls it."""
import json, os, functools
HERE = os.path.dirname(os.path.abspath(__file__)); SCHEMA = os.path.join(os.path.dirname(HERE), "schema")


@functools.lru_cache(maxsize=None)
def _schema(kind):
    return json.load(open(os.path.join(SCHEMA, f"{kind}.schema.json")))


def validate(kind, obj):
    import jsonschema
    jsonschema.validate(obj, _schema(kind))
    return obj
