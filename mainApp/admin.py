from django.contrib import admin
from mainApp.models.UserProfile import Profile
from mainApp.models.Medicine import Medicine
from mainApp.models.DoctorPrescription import DoctorPrescription
from mainApp.models.AppointmentRecord import AppointmentRecord
from mainApp.models.Condition import Condition
from mainApp.models.RateRecord import RateRecord
from mainApp.models.OrderRecord import OrderRecord
from django_reverse_admin import ReverseModelAdmin


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'sex', 'role', 'doctor_rating')
    list_display_links = ['user']
    list_editable = ('name', 'sex', 'doctor_rating')


class CustomMedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'price', 'supply_num')
    list_display_links = ['id']
    list_editable = ('name', 'img', 'price', 'supply_num')


# Register your models here.注册
admin.site.register(Profile, CustomerProfileAdmin)
admin.site.register(Medicine, CustomMedicineAdmin)
admin.site.register(DoctorPrescription)
admin.site.register(AppointmentRecord)
admin.site.register(Condition)
admin.site.register(RateRecord)
admin.site.register(OrderRecord)
