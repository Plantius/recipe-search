from sqlmodel import Session

from app.core.database import engine
from app.core.models.ingredient import Ingredient
from app.core.models.links import RecipeIngredientLink, RecipeTagLink
from app.core.models.recipe import Recipe
from app.core.models.tag import Tag
from app.core.models.types import Unit


def seed_db():
    with Session(engine) as session:
        # Ingredients
        flour = Ingredient(name="flour")
        eggs = Ingredient(name="eggs")
        milk = Ingredient(name="milk")
        sugar = Ingredient(name="sugar")

        session.add_all([flour, eggs, milk, sugar])
        session.commit()

        # Tags
        breakfast = Tag(name="breakfast")
        dessert = Tag(name="dessert")

        session.add_all([breakfast, dessert])
        session.commit()

        # Recipes
        pancake = Recipe(name="Pancakes", description="Fluffy pancakes")

        session.add(pancake)
        session.commit()

        # Link ingredients
        session.add_all(
            [
                RecipeIngredientLink(
                    recipe_id=pancake.id,
                    ingredient_id=flour.id,
                    quantity=200,
                    unit=Unit.GRAM,
                ),
                RecipeIngredientLink(
                    recipe_id=pancake.id,
                    ingredient_id=eggs.id,
                    quantity=2,
                    unit=Unit.PIECES,
                ),
                RecipeIngredientLink(
                    recipe_id=pancake.id,
                    ingredient_id=milk.id,
                    quantity=300,
                    unit=Unit.MILLILITER,
                ),
            ]
        )

        # Link tags
        session.add(
            RecipeTagLink(
                recipe_id=pancake.id,
                tag_id=breakfast.id,
            )
        )

        session.commit()
