from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('opt/', views.opt, name='opt'),
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('payship/', views.payship, name='payship'),
    path('product_list/', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
