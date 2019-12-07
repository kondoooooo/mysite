"""
投稿の管理機能を追加
モデルを登録(register)
"""

from django.contrib import admin
# models.pyのclass Post ( models.Model ):と連動
from.models import Post

admin.site.register(Post)
