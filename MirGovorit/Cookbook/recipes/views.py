from django.db.models import F, Subquery, Count, Q
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError, HttpResponseNotFound
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request):
    try:
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        if recipe_id is None or product_id is None or weight is None:
            return HttpResponseBadRequest("Missing required parameters.")

        try:
            recipe_id = int(recipe_id)
            product_id = int(product_id)
            weight = float(weight)
        except ValueError:
            return HttpResponseBadRequest("Invalid parameter values.")

        recipe = get_object_or_404(Recipe, id=recipe_id)
        product = get_object_or_404(Product, id=product_id)

        recipe_product, created = RecipeProduct.objects.update_or_create(
            recipe=recipe, product=product, defaults={'weight': weight}
        )

        return HttpResponse(f"Product {product.name} added/updated in recipe {recipe.name} with weight {weight}g.")
    except Exception as e:
        return HttpResponseServerError(f"Error: {e}")


def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    recipe = get_object_or_404(Recipe, id=recipe_id)

    for recipe_product in recipe.recipeproduct_set.all():
        recipe_product.product.times_cooked += 1
        recipe_product.product.save()

    return HttpResponse(f"Recipe {recipe.name} cooked successfully.")


def show_recipes_without_product(request):
    try:
        product_id = request.GET.get('product_id')

        if product_id is None:
            return HttpResponseBadRequest("Missing required parameter.")
        try:
            product_id = int(product_id)
        except ValueError:
            return HttpResponseBadRequest("Invalid parameter value. Product id should be integer")

        recipes = (
            Recipe.objects.all()
            .exclude(
                pk__in=RecipeProduct.objects.filter(
                    weight__gte=10, product_id=product_id)
            )
        )

        return render(request, 'show_recipes.html', {'recipes': recipes})
    except Exception as e:
        return HttpResponseServerError(f"Error: {e}")
