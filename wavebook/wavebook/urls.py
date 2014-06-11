from django.conf.urls import patterns, include, url
from core import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomePageView.as_view()),
    url(r'^trestles/', views.SpotView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
