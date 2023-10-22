from rest_framework import serializers
from users.models import StudentUser, ContactInfo, StudentPosition, Skill
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


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
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
    academic_status = serializers.StringRelatedField()
    employment_status = serializers.StringRelatedField()
    skills = SkillSerializer(many=True)

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
