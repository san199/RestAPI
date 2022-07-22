from django.urls import path
# from .views import 
from .views import (
    AppPostViews,AppPostViewsById
)

urlpatterns = [
   path('post/', AppPostViews.as_view()),
   path('post/<int:id>', AppPostViewsById.as_view()),
]
