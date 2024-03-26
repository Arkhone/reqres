single_user_schema = {
    "data": {
        "id": "int",
        "email": "string",
        "first_name": "string",
        "last_name": "string",
        "avatar": "string"
    },
    "support": {
        "url": "string",
        "text": "string"
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
    },
    "$id": "http://example.org/root.json#",
    "type": "object",
    "definitions": {},
    "$schema": "http://json-schema.org/draft-07/schema#"
}

s_user_not_schema = {}

list_res_schema = {
  "page": "int",
  "per_page": "int",
  "total": "int",
  "total_pages": "int",
  "data": [
    {
      "id": "int",
      "name": "string",
      "year": "int",
      "color": "string",
      "pantone_value": "string"
    }
  ]
}

single_res_schema = {
    "data": {
        "id": "int",
        "name": "string",
        "year": "int",
        "color": "string",
        "pantone_value": "string"
    },
    "support": {
        "url": "string",
        "text": "string"
    }
}

s_res_not_schema = {}

delayed_schema = {
  "page": "int",
  "per_page": "int",
  "total": "int",
  "total_pages": "int",
  "data": [
    {
      "id": "int",
      "email": "string",
      "first_name": "string",
      "last_name": "string",
      "avatar": "string"
    }
  ],
  "support": {
      "url": "string",
      "text": "string"
    }
}
