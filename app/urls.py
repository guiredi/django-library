from django.urls import path

from .views import (
    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView
)

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('create/', AuthorCreateView.as_view()),
    path('<pk>', AuthorDetailView.as_view()),
    path('<pk>/update/', AuthorUpdateView.as_view()),
    path('<pk>/delete/', AuthorDeleteView.as_view())
]
