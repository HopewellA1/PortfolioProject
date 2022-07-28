from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    #path('admin/', admin.site.urls),

    #Auth
    path('signup/',views.signupuser,name="signup"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('login/',views.loginuser,name="login"),

    #Todo
    path('',views.home,name="Todohome"),
    path('create/',views.createtodo,name="createtodo"),
    path('current/',views.current,name="current"),
    path('completed/',views.completed,name="completed"),
    path('todo/<int:todo_pk>', views.viewtodo,name="viewtodo"),
    path('todo/<int:todo_pk>/complete/', views.completetodo,name="completetodo"),
    path('todo/<int:todo_pk>/delete/', views.deletetodo,name="deletetodo"),


]