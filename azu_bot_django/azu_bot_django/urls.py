from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('menu/', include('menu.urls')),
    path('cafes/', include('cafe.urls')),
    path('cafes/<int:cafe_id>/tables/', include('tables.urls')),
    path('cafes/<int:cafe_id>/reservations/', include('reservation.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)