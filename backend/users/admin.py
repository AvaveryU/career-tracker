from django.contrib import admin
from .models import (
    StudentUser,
    ContactInfo,
    Skill,
    AcademicStatus,
    EmploymentStatus,
    User,
    StudentPosition,
    Position,
)


class StudentPositionInline(admin.TabularInline):
    model = StudentPosition
    extra = 1


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Персональная информация", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = (
        "get_full_name",
        "date_of_birth",
        "education_level",
        "grade",
        "academic_status",
        # "specialization",
        "work_experience",
        "employment_status",
        "city",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "student_info__contact_info__alternate_email",
        "city",
        "specialization",
    )

    list_filter = ("grade",)
    inlines = [StudentPositionInline]

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = "Имя Отвечство"

    def grade(self, obj):
        return obj.student_info.grade


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("alternate_email", "phone_number", "telegram_login")
    search_fields = ("alternate_email", "phone_number")


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


@admin.register(Position)
class PositionStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
