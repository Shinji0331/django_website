from django.urls import path

# 作成したViewを読み込む
from .views import IndexView , AboutView

urlpatterns = [
    # URLパターンと呼び出すViewを定義
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
]
