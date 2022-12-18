

def GET_RESPONSE(code: str,
                 data: dict,
                 articeID: int,
                 liked: bool) -> dict:
    return {"code": code,
            "data": data,
            "articleID": articeID,
            "liked": liked}
