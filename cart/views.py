from django.shortcuts import render, HttpResponse
from downloads.models import Songs
from User.models import User
from cart.models import CartItem


def cart(request):
    u = User.objects.get(pk=request.session['m_id'])
    if 'cart' in request.GET and request.GET['cart']:
        cart = request.GET['cart']
        cart = cart.split(',')
        for id in cart:
            song = Songs.objects.get(id=id)
            try:
                CartItem.objects.get(song=song)
            except CartItem.DoesNotExist:
                c = CartItem(user=u, song=song)
                c.save()
        csongs = CartItem.objects.filter(user=u)
        context = {'csongs': csongs}
        template = 'cart.html'
        return render(request, template, context)
    else:
        csongs = CartItem.objects.filter(user=u)
        context = {'csongs': csongs}
        template = 'cart.html'
        return render(request, template, context)