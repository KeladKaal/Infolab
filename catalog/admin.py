from django.contrib import admin
from .models import Clubs
#from .models import Creativedirsclass
#from .models import Trenddirsclass

admin.site.register(Clubs)
#admin.site.register(Creativedirsclass)
#admin.site.register(Trenddirsclass)
from .models import Profile#, Clubs

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

class ClubsAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'leader_id']

admin.site.register(Profile, ProfileAdmin)
