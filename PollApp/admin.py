from django.contrib import admin
from . models import Questions, Choices

class QuestionsAdmin(admin.ModelAdmin):
	list_display=('question_text','publish')


class ChoicesAdmin(admin.ModelAdmin):
	list_display=('choice_text','vote')

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.site_header='Poll App'
admin.site.site_title='Poll Admin Area'
admin.site.index_title='Welcome to Poll Admin Panel'
