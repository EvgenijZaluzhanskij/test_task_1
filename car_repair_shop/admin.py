from django.contrib import admin
from django.forms import ModelChoiceField
from car_repair_shop.models import Client, Master, Order


class ClientChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return str(obj)


class ClientAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'client_id':
            return ClientChoiceField(queryset=Client.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class MasterAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'master_id':
            return ClientChoiceField(queryset=Master.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Order, OrderAdmin)
