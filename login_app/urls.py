from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from login_app import views
urlpatterns=[
    path('login/',views.Create), #views.function_nm from views
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('google-login/', views.google_login, name='google_login'),
    path('delete/<rid>',views.delete)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)