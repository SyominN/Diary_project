from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('posts.urls', namespace='posts')),
    path('auth/', include('users.urls', namespace='users')),
]

urlpatterns += [
    path('auth/', include('django.contrib.auth.urls'))
]
