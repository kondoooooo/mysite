from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# インデックスページ
def index(request):
    # return HttpResponse("Hello World! このページは投稿のインデックスです。")
    # Postのclassから全てのobjectsを取り出し、最新のものから並べ替え
    posts = Post.objects.order_by("-published")
    """"
    {'テンプレ内での変数名':渡す変数名}
     posts/index.htmlを呼び出すときに
     postsという変数にデータを持っている状態で、このテンプレートが呼び出される
    """
    return render ( request, 'posts/index.html', {'posts': posts} )


def post_detail(request,post_id):
    # 投稿した番号の数字がない場合404のページを出す
    # プライマリーキーにpost_id
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})  # postのobjectsを渡す
# Create your views here.
