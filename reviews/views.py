from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect

from .models import Review


class ReviewListView(View):

    def get(self, request):

        reviews = Review.objects.all()

        return render(request, 'reviews/reviews.html', {
            'reviews': reviews
        })

    def post(self, request):

        nombre = request.POST.get('nombre')
        comentario = request.POST.get('comentario')
        estrellas = request.POST.get('estrellas')

        imagen = request.FILES.get('imagen')

        Review.objects.create(
            nombre=nombre,
            comentario=comentario,
            estrellas=estrellas,
            imagen=imagen
        )

        return redirect('reviews')
# Create your views here.
