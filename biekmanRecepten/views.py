from django.shortcuts import render
from .models import Recipe

# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_recipe(request):
    if request.method == 'POST':
        if request.POST.get("submit"):
            recipe = Recipe()
            recipe.title = request.POST['title']
            recipe.dish = request.POST['dish']
            recipe.season = request.POST['season']
            recipe.prep_time = request.POST['prep_time']
            recipe.description = request.POST['description']
            recipe.people = request.POST['people']
            recipe.save()
    dish = ["Vlees", "Vis", "Vegetarisch", "Seafood", "Dessert", "Apperatief", "Anders"]
    seasons = ["Winter", "Lente", "Zomer", "Herfst", "Meerdere seizoenen"]
    return render(request, 'add_recipe.html', {
        'dish': dish,
        'seasons': seasons,
    })
