from django.urls import path
from .views import insertRecord,months,monthDetails,calculationsView,finalAmounts,home,contactUs,updateRecord
urlpatterns = [
    path('insertRecords/',insertRecord,name='insertRecords'),
    path('months',months,name = 'months'),
    path('monthDetails/<int:id>',monthDetails,name = 'monthDetails'),
    path('calculation/',calculationsView,name = 'calculations'),
    path('finalAmounts/',finalAmounts,name = 'finalAmounts'),
    path('',home,name='home'),
    path('aboutUs/',contactUs,name = 'contactus'),
    path('updateRecord/<int:uid>/',updateRecord,name = 'updateRecord'),


]
