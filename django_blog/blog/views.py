from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

from .forms import RegistrationForm, UserUpdateForm, ProfileForm 
from .models import Post, Comment
from .forms import PostForm, CommentForm

# --- Auth views using Django built-ins ---
class UserLoginView(LoginView):
    template_name = "blog/login.html"

class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"


# --- Custom registration ---
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately after registration
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegistrationForm()
    return render(request, "blog/register.html", {"form": form})


# --- Profile (view + edit) ---
@login_required
def profile_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    return render(request, "blog/profile.html", {"u_form": u_form, "p_form": p_form})


# --- (Optional) simple Home view so navbar links work ---
def home_view(request):
    return render(request, "blog/home.html")

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-published_date"]  # newest first

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Authenticated users can create; author set in form_valid
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created.")
        return super().form_valid(form)

# Only the author can edit/delete
class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("posts")

    def form_valid(self, form):
        messages.success(self.request, "Post updated.")
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("posts")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(request, *args, **kwargs)
    
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        return redirect('post-detail', pk=post.id)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('post-detail', pk=comment.post.id)

    def test_func(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('post-detail', pk=post_id)

    def test_func(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return self.request.user == comment.author
    
def search_posts(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag_name})
