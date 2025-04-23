from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from market.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('market.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('subscriptions.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
