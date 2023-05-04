from django.contrib import admin
from .models import phone,Service,profileimage,contact_us,Apple,Types

# Register your models here.
admin.site.register(phone)
admin.site.register(Apple)
admin.site.register(Types)
admin.site.register(Service)
admin.site.register(profileimage)
admin.site.register(contact_us)


