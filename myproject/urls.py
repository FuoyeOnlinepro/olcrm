from django.contrib import admin
from django.urls import path, include
from onlinecourseregistration.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourseregistration/', include('onlinecourseregistration.urls')),
    path('', HomeView.as_view(), name='home'),
]
