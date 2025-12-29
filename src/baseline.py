import json
from typing import List, Dict, Set

def load_foods(path: str) -> List[Dict]:
    """
    load good items from JSON file
    """
    with open(path, "r") as f:
        foods = json.load(f)
        return foods
    
def filter_foods(foods: List[Dict], disliked_food_ids: Set[str], dietary_restrictions: Set[str]) -> List[Dict]:
    """
    Remove foods that violate hard constraints
    """
    filtered = []
    for food in foods:
        if food["id"] in disliked_food_ids:
            continue

        if dietary_restrictions:
            if not dietary_restrictions.issubset(set(food["dietary_tags"])):
                continue
        
        filtered.append(food)

    return filtered

def compute_preference_score(food: Dict, liked_food_ids: Set[str], base_score: float = 1.0, liked_bonus: float = 2.0) -> float:
    score = base_score
    if food["id"] in liked_food_ids:
        score += liked_bonus

    return score

def select_foods_under_budget(foods: List[Dict], liked_food_ids: Set[str], budget: float) -> List[Dict]:
    scored_foods = []
    for food in foods:
        score = compute_preference_score(food, liked_food_ids)
        scored_foods.append((score, food))
    scored_foods.sort(key = lambda x: x[0], reverse = True)

    selected = []
    total_cost = 0.0
    for _, food in scored_foods:
        cost = food["cost_per_unit"]
        if total_cost + cost <= budget:
            selected.append(food)
            total_cost += cost

    return selected

def compute_nutrition_summary(selected_foods: List[Dict]) -> Dict:
    summary = {"calories": 0.0, "protein": 0.0, "carbs": 0.0, "fat": 0.0,}
    for food in selected_foods:
        summary["calories"] += food["calories_per_unit"]
        summary["protein"] += food["protein_per_unit"]
        summary["carbs"] += food["carbs_per_unit"]
        summary["fat"] += food["fat_per_unit"]
    return summary

if __name__ == "__main__":
    foods = load_foods("data/foods.json")
    disliked_food_ids = {"food_003"}
    dietary_restrictions = {"vegetarian"}
    liked_food_ids = {"food_001", "food_005"}
    budget = 5.0
    filtered_foods = filter_foods(foods, disliked_food_ids, dietary_restrictions,)
    selected_foods = select_foods_under_budget(filtered_foods, liked_food_ids, budget,)
    nutrition_summary = compute_nutrition_summary(selected_foods)
    print("selected foods:", selected_foods)
    print("nutriotion summary:", nutrition_summary)

   