def cakes(recipe, available):
    amount = {}
    for r,e in recipe.items():
        if r in available:
            amount[r] = available[r] // e
        else: 
            return 0
    return min(amount.values())
​
​