from django.contrib.auth.models import AbstractUser
from django.db import models

from core.texts import (
    ACADEMIC_STATUS_CHOICES,
    EDUCATION_LEVELS,
    EMPLOYMENT_STATUS_CHOICES,
    GRADE_CHOICES,
    POSITION_LIST,
    NAME_LEN,
    PHONE_LEN,
    MAIL_LEN,
    TELEGRAM_LEN,
    BASIC_LEN,
)
from .validators import validate_not_me, UsernameValidator


class User(AbstractUser):
    email = models.EmailField(
        "Электронная почта",
        max_length=MAIL_LEN,
        unique=True,
    )

    username = models.CharField(
        "Имя пользователя",
        max_length=NAME_LEN,
        unique=True,
        db_index=True,
        validators=[
            validate_not_me,
            UsernameValidator,
        ],
        error_messages={
            "unique": "Пользователь с таким именем уже существует.",
        },
    )

    first_name = models.CharField(
        "Имя",
        max_length=NAME_LEN,
    )

    last_name = models.CharField(
        "Фамилия",
        max_length=NAME_LEN,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=("username", "email"), name="unique_username_email"
            )
        ]

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def __str__(self):
        return self.get_full_name()


class ContactInfo(models.Model):
    """
    Модель для контактной информации.
    """

    phone_number = models.CharField(
        max_length=PHONE_LEN,
        unique=True,
        verbose_name="Номер телефона",
    )
    alternate_email = models.EmailField(
        max_length=MAIL_LEN,
        unique=True,
        verbose_name="Дополнительный адрес электронной почты",
    )
    telegram_login = models.CharField(
        max_length=TELEGRAM_LEN,
        blank=True,
        null=True,
        verbose_name="Логин в Telegram",
    )

    def __str__(self):
        return self.email


class Skill(models.Model):
    """
    Модель для навыков.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        verbose_name="Навык",
    )

    def __str__(self):
        return self.name


class AcademicStatus(models.Model):
    """
    Модель для статуса обучения.
    """

    name = models.CharField(
        max_length=NAME_LEN,
        choices=ACADEMIC_STATUS_CHOICES,
        verbose_name="Учебный статус",
    )

    def __str__(self):
        return self.name


class EmploymentStatus(models.Model):
    """
    Модель для статуса трудоустройства.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        choices=EMPLOYMENT_STATUS_CHOICES,
        verbose_name="Статус трудоустройства",
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    """
    Модель выбора ожидаемой должности.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        choices=POSITION_LIST,
        verbose_name="Должность",
    )


class StudentUser(models.Model):
    """
    Расширенная модель пользователя для студента.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_info",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
    )
    education_level = models.CharField(
        max_length=100,
        choices=EDUCATION_LEVELS,
        blank=True,
        null=True,
        verbose_name="Уровень образования",
    )

    # Наследуемые поля
    contact_info = models.OneToOneField(
        ContactInfo,
        on_delete=models.CASCADE,
        verbose_name="Контактная информация",
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="students",
        blank=True,
        verbose_name="Навыки",
    )
    academic_status = models.ForeignKey(
        AcademicStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Учебный статус",
    )
    employment_status = models.ForeignKey(
        EmploymentStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Статус трудоустройства",
    )

    # Дополнительные поля
    city = models.CharField(
        max_length=BASIC_LEN,
        blank=True,
        null=True,
        verbose_name="Город",
    )
    specialization = models.CharField(
        max_length=BASIC_LEN,
        blank=True,
        null=True,
        verbose_name="Специализация",
    )
    work_experience = models.CharField(
        max_length=BASIC_LEN,
        blank=True,
        null=True,
        verbose_name="Опыт работы",
    )
    grade = models.CharField(
        max_length=BASIC_LEN,
        choices=GRADE_CHOICES,
        blank=True,
        null=True,
        verbose_name="Грэйд",
    )
    positions = models.ManyToManyField(
        Position,
        verbose_name="Предпочтительные должности",
        blank=True,
    )

    REQUIRED_FIELDS = [
        "date_of_birth",
        "contact_info__phone_number",
    ]

    def __str__(self):
        return self.user.get_full_name()


# class RecruiterUser(User):
#     """Модель пользователя-рекрутера."""
#
#     user = models.OneToOneField(
#         CustomUser, on_delete=models.CASCADE, primary_key=True
#     )
#     company_name = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True,
#         verbose_name="Название компании",
#     )
#     phone_number = models.CharField(
#         max_length=15,
#         blank=True,
#         null=True,
#         verbose_name="Номер телефона",
#     )
#     job_postings = models.ManyToManyField(
#         JobPosting,
#         related_name="recruiters",
#         blank=True,
#         verbose_name="Вакансии",
#     )
#     candidates = models.ManyToManyField(
#         StudentUser,
#         related_name="recruiters",
#         blank=True,
#         verbose_name="Студенты",
#     )

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = [
#         "company_name",
#         "phone_number",
#         "first_name",
#         "last_name",
#     ]

#     class Meta:
#         verbose_name = "Компания"
#         verbose_name_plural = "Компании"
#         constraints = [
#             models.UniqueConstraint(
#                 fields=("company_name", "email"),
#                 name="unique_company_name_email",
#             )
#         ]

#     def __str__(self) -> str:
#         return self.company_name
