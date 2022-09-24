from django.shortcuts import render
from.models import Blog_Post
# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from.form import Newpostform
from django.views import generic
from django.urls import reverse_lazy

# def post_blog_view(request):
#     post = Blog_Post.objects.filter(status='pub')
#     return render(request, 'blogt/post.html', {'post': post})
class PostlistViews(generic.ListView):
    # model = Blog_Post
    template_name = 'blogt/post.html'
    context_object_name = 'post'
    def get_queryset(self):
        return Blog_Post.objects.filter(status='pub').order_by('-datetime_modified')

# def post_blog_detial(request, pk):
#     post = get_object_or_404(Blog_Post, pk=pk)
#     # try:
#     #     post = Blog_Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     return render(request, 'blogt/home.html', {'post': post})
class DetailPostViews(generic.DetailView):
    model = Blog_Post
    template_name = 'blogt/home.html'
    context_object_name = 'post'

# def create_post_form(request):
#     # print(request.method)
#     if request.method == 'POST':
#         form = Newpostform(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('blog')
#
#     else:
#         form = Newpostform()
#     return render(request, 'blogt/form.html', {'form': form})
class CreatPostView(generic.CreateView):
    model = Blog_Post
    form_class = Newpostform
    template_name = 'blogt/form.html'
# def update_postdetail(request, pk):
#     post = get_object_or_404(Blog_Post, pk=pk)
#     form = Newpostform(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#     return render(request, 'blogt/form.html', {'form': form})
class UpdateListView(generic.UpdateView):
    model = Blog_Post
    form_class = Newpostform
    template_name = 'blogt/form.html'

# def delete_post_view(request, pk):
    # post = get_object_or_404(Blog_Post, pk=pk)
class DeletePostViewes(generic.DeleteView):
    model = Blog_Post
    template_name = 'blogt/form.html'
    success_url = reverse_lazy('blog')









