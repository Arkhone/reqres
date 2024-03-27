create_schema = {
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ],
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    }
}

reg_schema = {
    "required": [
        "id",
        "token"
    ],
    "properties": {
        "id": {"type": "integer"},
        "token": {"type": "string"}
    }
}

reg_unsuccess_schema = {
    "required": ["error"],
    "properties": {
        "error": {"type": "string"}
    }
}

login_schema = {
    "required": ["token"],
    "properties": {
        "token": {"type": "string"}
    }
}

login_unsucc_schema = {
    "required": ["error"],
    "properties": {
        "error": {"type": "string"}
    }
}
