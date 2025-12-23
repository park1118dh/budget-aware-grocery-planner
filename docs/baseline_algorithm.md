# Baseline Grocery List Algorithm

This document describes a deterministic baseline algorithm for
generating grocery lists without the use of machine learning.

The purpose of this algorithm is to demonstrate that the system
functions correctly using explicit constraints and scoring logic.

---

## Phase 1: Constraint Filtering

From the full food database, remove all food items that violate
hard constraints:

- Exclude any food whose `id` appears in the user's disliked food list.
- Exclude any food whose `dietary_tags` conflict with user dietary
  restrictions.

The result is a filtered candidate food set.

---

## Phase 2: Preference Scoring

For each remaining food item, compute a preference score:

- If the food is explicitly liked by the user, assign a higher
  preference weight.
- If the food is neutral (neither liked nor disliked), assign a
  baseline preference weight.

This produces a numeric preference score for each candidate food.

---

## Phase 3: Budget-Constrained Selection

Sort candidate food items by descending preference score.

Iteratively add food items to the grocery list in that order,
assigning a default quantity per item, until adding the next item
would exceed the user-defined budget.

This step ensures:
- The budget constraint is never violated.
- Highly preferred foods are prioritized.

---

## Phase 4: Nutritional Adjustment

After initial selection, adjust quantities of selected food items
to improve alignment with nutritional targets:

- Increase quantities of foods that contribute to underrepresented
  macronutrients.
- Decrease quantities of foods that overshoot nutritional targets,
  while preserving preference ordering.

No new food items are introduced during this phase.