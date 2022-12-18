def LOGIN(username: str,
          password: str) -> dict:
    return {"type": "login",
            "data": {"username": username,
                     "password": password}}


def REGISTER(username: str,
             password: str) -> dict:
    return {"type": "register",
            "data": {"username": username,
                     "password": password}}


def PING() -> dict:
    return {"type": "ping"}


def LIKE(username: str,
         articleID: int) -> dict:

    return {"type": "like",
            "data": {"username": username,
                     "articleID": articleID}}


def GET(username: str,
        isRandom: bool, 
        articleID: int = 0) -> dict:

    return {"type": "get",
            "data": {"username": username,
                     "isRandom": isRandom,
                     "articleID": articleID}}
