from django.urls import path

from . import views

# viewsのindexを呼び出して、関数の中を実行する
# urlpatterns = [url ( r'^$', views.index, name='index' )]
urlpatterns = [
    path ( '', views.index, name='index' ),
]
