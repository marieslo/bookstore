        if OneTimeCode.objects.filter(user__email=email, code=code).exists():
            user = User.objects.get(email=email)
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class AdvertisementCreate(LoginRequiredMixin, CreateView):
    form_class = AdvertisementForm
    model = Advertisement
    template_name = 'advertisement/create.html'

def form_valid(self, form):
        post = form.save(commit=False)
        post.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)


class AdvertisementView(ListView):
    model = Advertisement
    template_name = 'advertisement/list.html'
    ordering = '-time_create'
    context_object_name = 'post_list'


def advertisement_detail(request, post_id):
    post = get_object_or_404(Advertisement, pk=post_id)
    replies = post.replies.count
    new_reply = None
    if request.method == 'POST':
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            new_reply.post = post
            new_reply.user = User.objects.get(id=request.user.id)
            new_reply.save()
    else:
        reply_form = ReplyForm()
    return render(request, 'advertisement/post.html', {'post': post, 'replies': replies, 'new_reply': new_reply, 'reply_form': reply_form})

