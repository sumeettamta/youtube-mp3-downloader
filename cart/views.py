from django.shortcuts import render, HttpResponse
from downloads.models import Songs, UserHistory
from User.models import User
from cart.models import CartItem
from cart.serializers import CartSerializer
from rest_framework import generics


def cart(request):
    csongs = []
    u = User.objects.get(pk=request.session['m_id'])
    if 'rcart' in request.GET and request.GET['rcart']:
        cs = Songs.objects.get(id=request.GET['rcart'])
        cart = CartItem.objects.get(user=u)
        cart.song.remove(cs)
    if 'cart' in request.GET and request.GET['cart']:
        cs = Songs.objects.get(id=request.GET['cart'])
        cart, created = CartItem.objects.get_or_create(user=u)
        cart.save()
        cart.song.add(cs)
    try:
        uc = CartItem.objects.get(user__id=request.session['m_id'])
        csongs = uc.song.all()
        return render(request, 'cart.html', {'csongs': csongs})
    except:
        return render(request, 'cart.html', {'csongs': csongs})


def checkout(request):
    csongs = []
    if 'm_id' in request.session:
        user = User.objects.get(id=request.session['m_id'])
        print user
        try:
            uh = UserHistory.objects.get(user__id=request.session['m_id'])
        except:
            uh = UserHistory(user=user)
            uh.save()
        uc = CartItem.objects.get(user__id=request.session['m_id'])
        csongs = uc.song.all()
        for csong in csongs:
            uh.song.add(csong)
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
