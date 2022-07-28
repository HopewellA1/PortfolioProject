from django.contrib import admin
from django.urls import path
from Blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('Blog',views.home,name='Blogs'),
    path('<int:blog_id>/',views.blogDetail,name='blogDetail')
    #path('blog/', include('blog.urls'))
]