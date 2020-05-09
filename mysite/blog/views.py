from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
# models 에서 정의한 Post 의 DB 를 참조

# Create your views here.

def post_list(request):     # post_list 는 request 값을 받아
    posts = Post.objects.filter(updated__lte=timezone.now()).order_by('-updated')

    # post db 의 내용을 시간순으로 정렬해서 posts ( <- 쿼리셋 이름 ) 에 담음

    return render(request, 'blog/post_list.html', {'posts':posts})

    # reder 메서드 호출해 받아낸 blog/post_list.html 이라는 템플릿을 출력

def post_detail(request, pk):     # post_detail 는 request 와 pk 값을 받아
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_nick = request.user
            post.updated = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_nick = request.user
            post.updated = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})