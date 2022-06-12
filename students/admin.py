from django.contrib import admin

from students.models import OneCourseVideo, TwoCourseVideo, MetodicalOneCourses, MetodicalTwoCourses

admin.site.register(OneCourseVideo)
admin.site.register(TwoCourseVideo)
admin.site.register(MetodicalOneCourses)
admin.site.register(MetodicalTwoCourses)