from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UsernameValidator(RegexValidator):
    regex = r"^[\w]+[^@\.\+\-]*$"
    message = (
        "Неверное имя пользователя. "
        "Допускаются только буквы, цифры и знак подчеркивания."
        " Не может содержать символы «@», «.», «+» или «-»."
    )


def validate_not_me(value):
    if value.lower() == "me":
        raise ValidationError("Имя пользователя 'me' недопустимо.")
