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
                "id": {
                    "$id": "#/properties/data/properties/id",
                    "type": "integer"
                },
                "email": {
                    "$id": "#/properties/data/properties/email",
                    "type": "string"
                },
                "first_name": {
                    "$id": "#/properties/data/properties/first_name",
                    "type": "string"
                },
                "last_name": {
                    "$id": "#/properties/data/properties/last_name",
                    "type": "string"
                },
                "avatar": {
                    "$id": "#/properties/data/properties/avatar",
                    "type": "string"
                }
            },
            "$id": "#/properties/data",
            "type": "object"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "$id": "#/properties/support/properties/url",
                    "type": "string"
                },
                "text": {
                    "$id": "#/properties/support/properties/text",
                    "type": "string"
                }
            },
            "$id": "#/properties/support",
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
        "page": {
            "$id": "#/properties/page",
            "type": "integer"
        },
        "per_page": {
            "$id": "#/properties/per_page",
            "type": "integer"
        },
        "total": {
            "$id": "#/properties/total",
            "type": "integer"
        },
        "total_pages": {
            "$id": "#/properties/total_pages",
            "type": "integer"
        },
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
                    "id": {
                        "$id": "#/properties/data/items/properties/id",
                        "type": "integer"
                    },
                    "email": {
                        "$id": "#/properties/data/items/properties/email",
                        "type": "string"
                    },
                    "first_name": {
                        "$id": "#/properties/data/items/properties/first_name",
                        "type": "string"
                    },
                    "last_name": {
                        "$id": "#/properties/data/items/properties/last_name",
                        "type": "string"
                    },
                    "avatar": {
                        "$id": "#/properties/data/items/properties/avatar",
                        "type": "string"
                    }
                },
                "$id": "#/properties/data/items",
                "type": "object"
            },
            "$id": "#/properties/data",
            "type": "array"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "$id": "#/properties/support/properties/url",
                    "type": "string"
                },
                "text": {
                    "$id": "#/properties/support/properties/text",
                    "type": "string"
                }
            },
            "$id": "#/properties/support",
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
        "page": {
            "$id": "#/properties/page",
            "type": "integer"
        },
        "per_page": {
            "$id": "#/properties/per_page",
            "type": "integer"
        },
        "total": {
            "$id": "#/properties/total",
            "type": "integer"
        },
        "total_pages": {
            "$id": "#/properties/total_pages",
            "type": "integer"
        },
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
                    "id": {
                        "$id": "#/properties/data/items/properties/id",
                        "type": "integer"
                    },
                    "name": {
                        "$id": "#/properties/data/items/properties/name",
                        "type": "string"
                    },
                    "year": {
                        "$id": "#/properties/data/items/properties/year",
                        "type": "integer"
                    },
                    "color": {
                        "$id": "#/properties/data/items/properties/color",
                        "type": "string"
                    },
                    "pantone_value": {
                        "$id": "#/properties/data/items/properties/pantone_value",
                        "type": "string"
                    }
                },
                "$id": "#/properties/data/items",
                "type": "object"
            },
            "$id": "#/properties/data",
            "type": "array"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "$id": "#/properties/support/properties/url",
                    "type": "string"
                },
                "text": {
                    "$id": "#/properties/support/properties/text",
                    "type": "string"
                }
            },
            "$id": "#/properties/support",
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
                "id": {
                    "$id": "#/properties/data/properties/id",
                    "type": "integer"
                },
                "name": {
                    "$id": "#/properties/data/properties/name",
                    "type": "string"
                },
                "year": {
                    "$id": "#/properties/data/properties/year",
                    "type": "integer"
                },
                "color": {
                    "$id": "#/properties/data/properties/color",
                    "type": "string"
                },
                "pantone_value": {
                    "$id": "#/properties/data/properties/pantone_value",
                    "type": "string"
                }
            },
            "$id": "#/properties/data",
            "type": "object"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "$id": "#/properties/support/properties/url",
                    "type": "string"
                },
                "text": {
                    "$id": "#/properties/support/properties/text",
                    "type": "string"
                }
            },
            "$id": "#/properties/support",
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
        "page": {
            "$id": "#/properties/page",
            "type": "integer"
        },
        "per_page": {
            "$id": "#/properties/per_page",
            "type": "integer"
        },
        "total": {
            "$id": "#/properties/total",
            "type": "integer"
        },
        "total_pages": {
            "$id": "#/properties/total_pages",
            "type": "integer"
        },
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
                    "id": {
                        "$id": "#/properties/data/items/properties/id",
                        "type": "integer"
                    },
                    "email": {
                        "$id": "#/properties/data/items/properties/email",
                        "type": "string"
                    },
                    "first_name": {
                        "$id": "#/properties/data/items/properties/first_name",
                        "type": "string"
                    },
                    "last_name": {
                        "$id": "#/properties/data/items/properties/last_name",
                        "type": "string"
                    },
                    "avatar": {
                        "$id": "#/properties/data/items/properties/avatar",
                        "type": "string"
                    }
                },
                "$id": "#/properties/data/items",
                "type": "object"
            },
            "$id": "#/properties/data",
            "type": "array"
        },
        "support": {
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "$id": "#/properties/support/properties/url",
                    "type": "string"
                },
                "text": {
                    "$id": "#/properties/support/properties/text",
                    "type": "string"
                }
            },
            "$id": "#/properties/support",
            "type": "object"
        }
    }
}
