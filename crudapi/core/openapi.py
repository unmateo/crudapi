from copy import deepcopy
from typing import Any
from typing import Dict
from typing import List


def combine(base: Dict[Any, Any], others: List[Dict[Any, Any]]):
    """Return a combination of OpenAPI specs."""
    openapi = deepcopy(base)
    paths = openapi.setdefault("paths", {})
    schemas = openapi.setdefault("components", {}).setdefault("schemas", {})
    for spec in others:
        for path, definition in spec["paths"].items():
            if path in paths:
                assert definition == paths[path]
            else:
                paths[path] = definition
        for schema, definition in spec["components"]["schemas"].items():
            if schema in schemas:
                assert definition == schemas[schema]
            else:
                schemas[schema] = definition
    return openapi
