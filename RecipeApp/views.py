from django.shortcuts import render, redirect
from RecipeApp.models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'RecipeApp/home.html', {'recipes': recipes})

def view_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'RecipeApp/recipe_view.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        Recipe.objects.create(
            title = title,
            description = description,
            ingredients = ingredients,
            instructions = instructions,
        )
        return redirect('home')
    return render(request, 'RecipeApp/add_recipe.html')

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('home')

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    print(request.POST)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_ingredients = request.POST.get('ingredients')
        new_instructions = request.POST.get('instructions')

        recipe.title = new_title
        recipe.description = new_description
        recipe.ingredients = new_ingredients
        recipe.instructions = new_instructions

        recipe.save()
        return redirect('home')
    return render(request, 'RecipeApp/update_recipe.html', {'recipe': recipe})