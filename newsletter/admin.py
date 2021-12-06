from django.contrib import admin
from newsletter.models import Subscripers, MailMessages

# Register your models here.
admin.site.register(Subscripers)
admin.site.register(MailMessages)
