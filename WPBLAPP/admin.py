from django.contrib import admin
from .models import User,Transaction,SADUser,SADtransaction
# Register your models here.

admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(SADUser)
admin.site.register(SADtransaction)