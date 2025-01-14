from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo

class IndexView(View):
    def get(self,request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request, "bookroute/index.html", {"datetime_now":datetime_now})
    
index = IndexView.as_view()
#indexviewクラスを関数に変換する
#bookroute/urls.pyのviews.indexはこれ

class PageCreateView(View):
    def get(self,request):#データを入力する画面を表示する
        form=PageForm()
        return render(request, "bookroute/page_form.html", {"form":form})
        #pageでユーザーが入力した項目がhtml側に渡される
        #bookroute/page_form.htmlの{{ form.as_p}}に渡される

    def post(self, request):#「登録」ボタンを押した後に動く
        form=PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("bookroute:index")#トップページにリダイレクト
            #このindexはbookrote/urls.pyのurlpatternsにあるname="index"
        return render(request, "bookrote/page_form.html", {"form":form})#入力(登録)に失敗すると入力画面に戻る
    
page_create=PageCreateView.as_view()


class PageListView(View):
    def get(self,request):
        page_list=Page.objects.order_by("-title")
        return render(request,"bookroute/page_list.html",{"page_list":page_list})
    
page_list=PageListView.as_view()


class PageDetailView(View):
    def get(self,request,id):
        page = get_object_or_404(Page, id=id)
        return render(request, "bookroute/page_detail.html", {"page":page})


page_detail=PageDetailView.as_view()


class PageUpdateView(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form =PageForm(instance=page)
        return render(request, "bookroute/page_update.html", {"form":form})
    
    def post(self, request, id):
        page=get_object_or_404(Page, id=id)
        form=PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("bookroute:page_detail", id=id)
        return render(request, "bookroute/page_update.html",{"form":form})
    
page_update=PageUpdateView.as_view()


