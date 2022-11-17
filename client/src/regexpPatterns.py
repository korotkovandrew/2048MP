# можно A-Z 0-9 _ , . -
# начинается с латинского символа
# длина от 6 до 32 символов
NICKNAME_RE_PATTERN = '^[a-zA-Z][a-zA-Z0-9_.,-]{5,31}$'
# NICKNAME_RE_PATTERN = '.*'

# любые латинские буквы
# как минимум одна цифра
# как минимум один спец символ
# длина от 8 до 20 символов
PASSWORD_RE_PATTERN = '((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{6,20})'
# PASSWORD_RE_PATTERN = '.*

#TODO расписать подробнее 
NICKNAME_VALIDATION_ERROR_MESSAGE = "Wrong nickname"
PASSWORD_VALIDATION_ERROR_MESSAGE = "Wrong password"
