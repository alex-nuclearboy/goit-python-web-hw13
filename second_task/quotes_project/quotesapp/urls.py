from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    # General path to home page
    path('', views.main, name='index'),

    # Tag management paths
    path('tag/', views.add_tag, name='add_tag'),
    path('tag/<int:tag_id>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('tag/delete/<int:tag_id>/', views.delete_tag, name='delete_tag'),

    # Author management paths
    path('author_form/', views.add_author, name='add_author'),
    path('author/<int:author_id>', views.author_detail, name='author_detail'),
    path(
        'author/edit/<int:author_id>/', views.edit_author, name='edit_author'
    ),
    path(
        'author/delete/<int:author_id>/', views.delete_author,
        name='delete_author'
    ),

    # Quote management paths
    path('quote_form/', views.add_quote, name='add_quote'),
    path(
        'quote/edit/<int:quote_id>/', views.edit_quote, name='edit_quote'
    ),
    path(
        'quote/delete/<int:quote_id>/', views.delete_quote, name='delete_quote'
    ),
]
