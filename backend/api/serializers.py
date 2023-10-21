from rest_framework import serializers
from users.models import (
    StudentUser,
    ContactInfo,
    StudentPosition,
)
from drf_extra_fields.fields import Base64ImageField


class StudentPositionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели StudentPosition, предоставляет имена позиции
    и академического статуса.
    """

    position_name = serializers.StringRelatedField(
        source="position", read_only=True
    )
    academic_status_name = serializers.StringRelatedField(
        source="academic_status", read_only=True
    )

    class Meta:
        model = StudentPosition
        fields = [
            "id",
            "position_name",
            "academic_status_name",
        ]


class ContactInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ContactInfo, предоставляет информацию
    о контактных данных.
    """

    class Meta:
        model = ContactInfo
        fields = [
            "phone_number",
            "alternate_email",
            "telegram_login",
        ]


class StudentUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели StudentUser, предоставляет данные о студентах.
    """

    user_id = serializers.IntegerField(source="user.id")
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    contact_info = ContactInfoSerializer()
    photo = Base64ImageField()
    training_status = StudentPositionSerializer(
        many=True, source="student_positions"
    )

    class Meta:
        model = StudentUser
        fields = [
            "user_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "photo",
            "training_status",
            "date_of_birth",
            "education_level",
            "city",
            "work_experience",
            "grade",
            "description",
            "resume",
            "contact_info",
            "academic_status",
            "employment_status",
            "skills",
        ]
