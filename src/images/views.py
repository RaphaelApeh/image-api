from django.shortcuts import render


def image_display_view(request):

    context = {}
    return render(request, 'images/base.html', context)