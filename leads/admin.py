from django.contrib import admin
from .models import Lead, User, Agent, UserProfile, Category

admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)