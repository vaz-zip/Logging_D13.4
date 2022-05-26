from django.urls import path
from .views import News, PostSearch, post_filter, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    UserUpdateView, IndexView, logging_page, test_error
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(News.as_view())),
    path('add/', PostCreateView.as_view(), name='_add'),
    path('<int:pk>/', cache_page(60 * 5)(PostDetailView.as_view()), name='post_detail'),
    path('search', post_filter),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('edit/', PostCreateView.as_view(), name='_edit'),
    path('search/', PostSearch.as_view(), name='_search'),
    path('user_edit/', UserUpdateView.as_view(), name='user_edit'),
    path('', IndexView.as_view()),
    path('logging_page/', logging_page, name='logging_page'),
    path('test_error', test_error, name='test_error'),
]
