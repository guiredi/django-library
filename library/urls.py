from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'v1/author', views.AuthorViewSet)
router.register(r'v1/book', views.BookViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# from django.contrib import admin
# from django.urls import path, include, re_path
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     path('api-auth/', include('rest_framework.urls')),
#     path('v1/', include('app.urls')),
#     path('admin/', admin.site.urls),
#     re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
# ]
