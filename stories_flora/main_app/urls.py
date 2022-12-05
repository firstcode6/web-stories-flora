from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoriesView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
    path('filter', views.FilterStoriesView.as_view(), name='filter'),

    path('story=<int:pk>/', views.StoryDetailView.as_view(), name='story_details'),
    path('story=<int:pk_st>/story_i18n=<int:pk>/', views.Story_i18nDetailView.as_view(), name='story_i18n_details'),

    path('story=<int:pk>/edit', views.StoryEditView.as_view(), name='edit_story'),
    path('story=<int:pk_st>/story_i18n=<int:pk>/edit', views.Story_i18nEditView.as_view(), name='edit_story_i18n'),
    path('story=<int:pk_st>/story_i18n=<int:pk_i18n>/page=<int:pk>-edit', views.PageEditView.as_view(), name='edit_page'),

    path('languages', views.LanguagesView.as_view(), name='language'),
    path('categories', views.CategoriesView.as_view(), name='category'),
    path('category=<int:pk>', views.CategoryDetailView.as_view(), name='category_details'),

   # path('category/<int:pk>/edit', views.CategoryEditView.as_view(), name='edit_category'),

    path('add-story', views.add_story, name='add_story'),
    path('story=<int:pk_st>/add-story-i18n', views.add_story_i18n, name='add_story_i18n'),
    path('story=<int:pk_st>/story_i18n=<int:pk_i18n>/add-page', views.add_page, name='add_page'),

    path('add-category', views.add_category, name='add_category'),

    path('login/', views.LoginUser.as_view(), name='login'),
]