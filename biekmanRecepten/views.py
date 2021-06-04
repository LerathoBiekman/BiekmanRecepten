from django.shortcuts import render
from .models import Recipe

# Create your views here.


def home(request):
    lists = get_lists("home")
    return render(request, 'home.html', {
        'seasons': lists[0],
        'meat': lists[1],
        'fish': lists[2],
        'veggie': lists[3],
        'continent': lists[4],
        'occasion': lists[5]
    })


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
    lists = get_lists("add_rcipe")
    return render(request, 'add_recipe.html', {
        'dish': lists[0],
        'seasons': lists[1],
    })


def search_engine(request):
    django_filter = Recipe.objects.filter()
    lists = get_lists("search_engine")
    return render(request, 'search_engine.html', {
        'dish': lists[0],
        'seasons': lists[1],
        'query': django_filter,
    })


def get_lists(page):
    dish = ["Vlees", "Vis", "Vegetarisch", "Seafood", "Dessert", "Apperatief", "Anders"]
    seasons = ["Winter", "Lente", "Zomer", "Herfst",]
    meat = ["kip", "varken", "rund", "gevolgte"]
    fish = ["Zalm", "Tilapia", "Zeebaars"]
    veggie = ["Soja", "Tofu", "Geen eiwitten"]
    continent = ["Afrika", "Europa", "Zuid-Amerika", "Azie", "Noord-Amerika", "Oceanie"]
    occasion = ["Verjaardag", "Moederdag", "Vaderdag", "Kerst", "Oud & Nieuw", "Pasen"]
    if page == "home":
        return seasons, meat, fish, veggie, continent, occasion
    return dish, seasons
