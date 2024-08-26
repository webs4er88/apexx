from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about', about, name='about'),
    path('carrer', carrer, name='carrer'),
    path('code-of-conduct', codeofconduct, name='codeofconduct'),
    path('contact', contact, name='contact'),
    path('freight-forwarding', freightforwarding, name='freightforwarding'),
    path('contact', contact, name='contact'),
    path('get-started', getstarted, name='getstarted'),
    path('grow-revenue', homepage, name='growrevenue'),
    path('platform', platform, name='platform'),
    path('privacy-policy', privacypolicy, name='privacypolicy'),
    path('supply-chain', supplychain, name='supplychain'),
    path('terms', terms, name='terms'),
    
    path('tracking', tracking, name='tracking' ),
    path('update-delivery-date/<tracking_number>/', update_delivery_date, name='update_delivery_date'),
]
