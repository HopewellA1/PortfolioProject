from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    #path('blog/', include('blog.urls'))
]