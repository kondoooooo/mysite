from django.db import models

"""
ブログの記事を格納するためのモデル
DBのデータを一つの変数として扱えるようなclassを定義
各種データを投入、編集、削除
"""


# Create your models here.
# 属性を宣言
class Post ( models.Model ):
    title = models.CharField ( max_length=100 )  # タイトル 文字列型CharField 文字数
    published = models.DateTimeField ()  # 記事が投稿された日
    image = models.ImageField ( upload_to='media/' )  # 画像データを保存する先
    body = models.TextField ()  # 本文 テキスト型 長めの文章

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]