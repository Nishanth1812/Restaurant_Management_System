from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('index.html', TemplateView.as_view(template_name='index.html'), name='index'),
    path('menu.html', TemplateView.as_view(template_name='menu.html'), name='menu'),
    path('orders.html', TemplateView.as_view(template_name='orders.html'), name='orders'),
    path('inventory.html', TemplateView.as_view(template_name='inventory.html'), name='inventory'),
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup.html', TemplateView.as_view(template_name='signup.html'), name='signup'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Serve frontend static files directly from root for development convenience
    from django.views.static import serve
    urlpatterns += [
        path('styles.css', serve, {'document_root': settings.BASE_DIR / 'frontend', 'path': 'styles.css'}),
        path('auth.js', serve, {'document_root': settings.BASE_DIR / 'frontend', 'path': 'auth.js'}),
        path('api.js', serve, {'document_root': settings.BASE_DIR / 'frontend', 'path': 'api.js'}),
        path('signup.js', serve, {'document_root': settings.BASE_DIR / 'frontend', 'path': 'signup.js'}),
        path('main.js', serve, {'document_root': settings.BASE_DIR / 'frontend', 'path': 'main.js'}),
        path('components/sidebar.html', serve, {'document_root': settings.BASE_DIR / 'frontend/components', 'path': 'sidebar.html'}),
    ]
