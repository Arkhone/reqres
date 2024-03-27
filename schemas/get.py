single_user_schema = {
    "required": [
        "data",
        "support"
    ],
    "properties": {
        "data": {
            "required": [
                "id",
                "email",
                "first_name",
                "last_name",
                "avatar"
            ],
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
            },
            "type": "object"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "type": "object"
        }
    }
}

list_users_schema = {
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ],
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "items": {
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar"
                ],
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string" },
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"}
                },
                "type": "object"
            },
            "type": "array"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "type": "object"
        }
    }
}

s_user_not_schema = {
    "required": [],
    "properties": {},
    "type": "object",
    "definitions": {}
}

list_res_schema = {
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ],
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "items": {
                "required": [
                    "id",
                    "name",
                    "year",
                    "color",
                    "pantone_value"
                ],
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "year": {"type": "integer"},
                    "color": {"type": "string"},
                    "pantone_value": {"type": "string"}
                },
                "type": "object"
            },
            "type": "array"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "type": "object"
        }
    }
}

single_res_schema = {
    "required": [
        "data",
        "support"
    ],
    "properties": {
        "data": {
            "required": [
                "id",
                "name",
                "year",
                "color",
                "pantone_value"
            ],
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "color": {"type": "string"},
                "pantone_value": {"type": "string"}
            },
            "type": "object"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "type": "object"
        }
    }
}

s_res_not_schema = {
    "required": [],
    "properties": {},
    "type": "object",
    "definitions": {}
}

delayed_schema = {
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ],
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "items": {
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar"
                ],
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"}
                },
                "type": "object"
            },
            "type": "array"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "type": "object"
        }
    }
}
