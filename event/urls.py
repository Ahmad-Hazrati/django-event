from . import views
from django.urls import path


urlpatterns = [
    path('', views.eventlist, name='home'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('like/<slug:slug>', views.event_like, name='event_like'),
    path('registeration_confirmation/<slug:slug>', views.registeration_confirmation, name='registeration-confirmation'),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete,
        name='comment_delete'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit,
        name='comment_edit'),
    path('category/<slug:cats>/', views.CategoryView, name='category'),
    path('search_events', views.search_events, name='search-events'),

]
