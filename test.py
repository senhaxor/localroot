def my_login(request):
    form = LoginForm(request.POST or None)
    template_name = 'accounts/login.html'

    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                request, username=form.username,
                password=form.password
            )
            auth_login(request, user)
            return HttpResponseRedirect(reverse('core:dashboard'))

    context = {'form': form}
    return render(request, template_name, context)
