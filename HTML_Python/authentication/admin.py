from django.contrib import admin

from authentication.models import User
from blog.models import Ticket, Critique


admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Critique)
