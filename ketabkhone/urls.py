from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_comment, bookdetail
from ketabkhone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookdetail/<int:book_id>/', views.bookdetail , name="bookdetail_page"),
    path('bookliste/', views.bookliste , name="booklist page"),
    path('contest/', views.contest , name="contest page"),
    path('category_bookliste/<int:category_id>/', views.category_bookliste , name="category_bookliste"),
    path('like/<int:book_id>/', views.like , name="book_like"),
    path('dislike/<int:book_id>/', views.dislike , name="book_dislike"),
    path('author_bookliste/<int:auth_id>/', views.author_list , name="author_list"),
    path('bookmark/<int:book_id>/', views.bookmark , name="book-bookmark"),
    path('login/',views.login_user , name="login_page"),
    path('new_register/',views.new_register , name="new_register"),
    path('add_comment/<int:book_id>/', views.add_comment , name="add_comment"),
    path('edit_comment/<int:book_id>/', views.edit_comment , name="edit_comment"),
    path('logout/',views.logout_user , name="logout"),
    path('profile/', views.profile , name="profile_page"),
    path('addbook/', views.addbook , name="addbook_page")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
