from django.contrib import admin
from .models import (
    StudentUser,
    ContactInfo,
    Skill,
    AcademicStatus,
    EmploymentStatus,
)


@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = (
        "get_full_name",
        "date_of_birth",
        "education_level",
        "employment_status",
    )
    search_fields = (
        "first_name",
        "last_name",
        "student_info__contact_info__email",
        "student_info__city",
        "student_info__specialization",
    )

    list_filter = ("grade",)

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = "ФИО"

    def grade(self, obj):
        return obj.student_info.grade


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "telegram_login")
    search_fields = ("email", "phone_number")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AcademicStatus)
class AcademicStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(EmploymentStatus)
class EmploymentStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
