from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=[
    'id','name','email','password','date','phone_no'
    ]

class MessageAdmin(admin.ModelAdmin):
    list_display=[
    'id','convo','sender','msg','time'
    ]

class FriendAdmin(admin.ModelAdmin):
    list_display = [
    'id','user1_id','user2_id','status','date'
    ]

class friend_messageAdmin(admin.ModelAdmin):
    list_display=[
    'id','friend_id','sender_id','date','message'
    ]

class GroupAdmin(admin.ModelAdmin):
    list_display=[
    'id','creater_id','name','title','created_date'
    ]

class ParticipantsAdmin(admin.ModelAdmin):
    list_display = [
    'id','group_id','participant_id'
    ]

class group_messageAdmin(admin.ModelAdmin):
    list_display = [
    'id','group_id','sender_id','message','date'
    ]

admin.site.register(User,UserAdmin)
admin.site.register(Friend,FriendAdmin)
admin.site.register(friend_message,friend_messageAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Participants,ParticipantsAdmin)
admin.site.register(group_message,group_messageAdmin)
admin.site.register(Message,MessageAdmin)
