from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from products.views import ProductListView



urlpatterns = [
    path('', ProductListView.as_view(), name='index'),#call the def after go to the url '' to give show the response
    path('users/login', views.login_view, name='login'),
    path('users/signup', views.signup, name='signup'),
    path('users/logout', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('productos/', include('products.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
