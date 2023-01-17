from django.contrib import admin
from .models import Poll, Choice, Vote


# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice



@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'pub_date')
    search_fields = ('question','user')
    list_filter = ['pub_date', ]
    inlines = [
        ChoiceInLine
    ]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_name','poll' )
    search_fields = ('choice_name',)
    list_filter = ['poll', ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll','choice','vote_user' )
    #search_fields = ('poll',)
    list_filter = ['poll','choice' ]




