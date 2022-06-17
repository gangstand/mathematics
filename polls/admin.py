from django.contrib import admin

from polls.models import Answer, Question, Result, Profile


class QuestionsInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class BookAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("profileid", "datetime", "username", "rating")

    def has_add_permission(self, request):
        return False


admin.site.register(Profile)
