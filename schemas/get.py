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
  ]
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
