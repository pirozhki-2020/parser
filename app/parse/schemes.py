from marshmallow import Schema, fields, post_load


class IngredientSchema(Schema):
    ingredient = fields.String()


class IngredientAmountSchema(Schema):
    ingredient_amount = fields.Float(data_key='ingredient amount')


class ToolSchema(Schema):
    tool = fields.String(data_key='tool')


class ToolAmountSchema(Schema):
    tool_amount = fields.Integer(data_key='tool-amount')


class RecipeStepSchema(Schema):
    recipe_step = fields.String(data_key='recipe-steps')


class CocktailSchema(Schema):
    name = fields.String(data_key='coctail')
    description = fields.String(data_key='coctail-description')
    image_link = fields.String(data_key='image')
    ingredients = fields.Nested(IngredientSchema, many=True,
                                data_key='ingredient')
    ingredients_amounts = fields.Nested(IngredientAmountSchema,
                                        many=True,
                                        data_key='ingredient amount')
    tools = fields.Nested(ToolSchema, many=True, data_key='tool')
    tools_amounts = fields.Nested(ToolAmountSchema, many=True,
                                  data_key='tool-amount')
    recipe_steps = fields.Nested(RecipeStepSchema, many=True,
                                 data_key='recipe-steps')


class ListCocktailSchema(Schema):
    cocktails = fields.Nested(CocktailSchema, many=True, data_key='cocktails')

    @post_load
    def flatten_date(self, data, **kwargs):
        cocktails = data['cocktails']
        for cocktail in cocktails:
            to_flatten = {'ingredients': 'ingredient',
                          'ingredients_amounts': 'ingredient_amount',
                          'tools': 'tool',
                          'tools_amounts': 'tool_amount',
                          'recipe_steps': 'recipe_step'}
            for k, v in to_flatten.items():
                cocktail[k] = [item[v] for item in
                               cocktail[k]]
        return data
