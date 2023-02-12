from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('scookie',views.setcookie),
    # path('gcookie',views.getcookie)

    #DELETING COOKIE

    path('testcookie/', views.cookie_session),
    path('deletecookie/', views.cookie_delete),
]
