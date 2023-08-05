create_schema = {
    "name": {"type": "string"},
    "job": {"type": "string"},
    "id": {"type": "string"},
    "createdAt": {"type": "string"}
}

registration_schema = {
    "id": "int",
    "token": "string"
}

registration_unsucc_schema = {
    "error": "string"
}

login_schema = {
    "token": "string"
}

login_unsucc_schema = {
    "error": "string"
}
