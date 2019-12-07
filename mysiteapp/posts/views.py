from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# models.pyのclass Postをインポート
from .models import Post


# インデックスページ
def index(request):
    # return HttpResponse("Hello World! このページは投稿のインデックスです。")
    # models.pyのclass Postから全てのオブジェクトを取り出し、最新のものから並べ替え
    posts = Post.objects.order_by("-published")
    """"
    HTMLのDB(posts)を呼び出す
        {'テンプレ内での変数名':渡す変数名}
        posts/index.htmlを呼び出すときに
        postsという変数にデータを持っている状態で、このテンプレートが呼び出される
    """
    return render ( request, 'posts/index.html', {'posts': posts} )


# 投稿ページの画面を扱う関数
def post_detail(request,post_id):
    # 投稿した番号の数字がない場合404のページを出す
    # プライマリーキーにpost_id
    post = get_object_or_404(Post, pk=post_id)
    # post_detail.htmlと連動
    return render(request, 'posts/post_detail.html', {'post': post})
