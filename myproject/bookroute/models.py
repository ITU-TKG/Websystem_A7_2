from django.db import models
import uuid
from pathlib import Path
#１つのページに１ルート表示。
#トップページにルート(通る店舗の順番)が表示されていて
#各ルートのページを見ればそのルートの詳細が見れるイメージ
class Page(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False ,verbose_name="id")
    #ルートid
    title=models.CharField(max_length=200, verbose_name="タイトル")
    #ページタイトル(通る店舗の順等の要素を含める)
    body=models.TextField(max_length=1000, verbose_name="本文")
    #本文。ルートの詳細とどこどこはよく混むなどの情報
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="作成日時")#作成日時
    updated_at=models.DateTimeField(auto_now=True, verbose_name="更新日時")#更新日時
    picture =models.ImageField(upload_to="bookroute/picture/", blank=True, null=True, verbose_name="写真")

    def __str__(self):
        return self.title
