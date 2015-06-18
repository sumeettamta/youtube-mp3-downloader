from django.shortcuts import render, HttpResponse
from downloads.models import Songs, UserHistory
from User.models import User
from cart.models import CartItem
from cart.serializers import CartSerializer
from rest_framework import generics


def cart(request):
    u = User.objects.get(pk=request.session['m_id'])
    if 'cart' in request.GET and request.GET['cart']:
        cart = request.GET['cart']
        cart = cart.split(',')
        for id in cart:
            song = Songs.objects.get(id=id)
            try:
                CartItem.objects.get(song=song, user=u)
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


def checkout(request):
    csongs = []
    uh = []
    if 'm_id' in request.session:
        print "hi"
        user = User.objects.get(id=request.session['m_id'])
        try:
            uh = UserHistory.objects.get(user__id=request.session['m_id'])
        except:
            uh = UserHistory(user=user)
            uh.save()
        csongs = CartItem.objects.filter(user__id=request.session['m_id'])
        for csong in csongs:
            uh.song.add(csong.song)
    CartItem.objects.filter(user__id=request.session['m_id']).delete()
    context = {'csongs': csongs}
    template = 'checkout.html'
    return render(request, template, context)


class CartList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer
