from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from .views import search_view ,custom_page_not_found
from django.conf.urls import handler404

handler404 = 'project.views.custom_page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_view, name='search'),
]

urlpatterns += i18n_patterns(
    path('set-language/', set_language, name='set_language'),
    path('', include('home.urls')),
    path('courses/', include('courses.urls')),
    path('python/', include('python.urls')),
    path('tools/', include('tools.urls')),
    path('books/', include('book.urls')),
    path('contact/', include('contact.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

