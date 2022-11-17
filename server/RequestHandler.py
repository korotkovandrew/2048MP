
#TODO реализовать поддержку всех запросов
# Поддерживаемые запросы:
# 'like' (username, article) -> bool
# 'log in' (username, password) -> bool
# 'sign in' (username, password) -> bool
# 'get random article' (-) -> article
# 'get recommended articles' (username, n) -> article в количестве n штук

class RequestHandler:
    def __init__(self, requestType, requestArgs):
        if requestType == 'like':
            pass
        elif requestType == 'log in':
            pass
        elif requestType == 'sign in':
            pass
        elif requestType == 'get random article':
            pass
        elif requestType == 'get recommended articles':
            pass