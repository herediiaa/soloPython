from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls'), name='blog')

]
