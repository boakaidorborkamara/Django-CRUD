from django.shortcuts import render
from django.views import generic


# Create your views here.
class PostListView (generic.PostListView):
    model = Post


class PostCreateView (generic.PostCreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)


class PostDetailView (generic.DetailView):
    model = Post


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)


class PostDeleteView(generic.DeleteView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)