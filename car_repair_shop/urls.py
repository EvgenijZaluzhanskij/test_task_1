from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^masters/$', views.list_masters, name='masters'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^order/$', views.order, name='order'),
    url(r'^order/make_order$', views.make_order, name='make_order')
]
