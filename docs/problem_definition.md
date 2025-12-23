# Problem Definition

## Problem Statement

Many people want their groceries to contain foods they enjoy, help meet their dietary goals, and remain under a reasonable budget. However, developing a grocery list that meet all these constraints involves non-trivial trade-offs between cost, nutrition, and food preferences.

This system is designed to help users choose what goes in their grocery lists. Given user inputted constraints and preferences, this system creates a grocery list that prioritizes food preference, while remaining under budget, and satisfying dietary goals and restrictions.


## User Inputs

The system accepts the following user inputs:

- Dietary goal  
  One of: lose weight, gain muscle, or maximize nutrition.  
  This goal influences how nutritional targets are interpreted but does
  not prescribe medical advice.

- Budget  
  A monetary budget over a specified time period (e.g., weekly, biweekly,
  or monthly). This budget is treated as a hard constraint.

- Foods the user enjoys  
  A list of food items the user prefers. These are treated as soft
  preferences and are prioritized during optimization when possible.

- Foods the user dislikes or wishes to avoid  
  A list of food items that must not appear in the generated grocery list.
  These are treated as hard constraints.

- Dietary restrictions (optional)  
  Constraints such as vegetarian, vegan, or lactose-free that must always
  be respected if provided.fajdoi
  


## System Outputs

The system produces the following outputs:

- Grocery list  
  A list of food items and associated quantities that satisfy all hard
  constraints and maximize the user preference score.

- Estimated total cost  
  The estimated monetary cost of the generated grocery list over the
  specified time period.

- Nutritional summary  
  An aggregate summary of estimated calories and macronutrients derived
  from the grocery list.

- Selection rationale  
  A brief explanation describing why key items or substitutions were
  selected, expressed in terms of user preferences, constraints, and
  optimization objectives.


## Optimization Objective

The system is formulated as a constrained optimization problem.

The primary objective is to maximize a quantified user preference score,
subject to the following hard constraints:

- The total estimated cost of the grocery list must not exceed the
  user-defined budget.
- Foods explicitly marked as disliked must not be included.
- Dietary restrictions must be respected at all times.

User preferences are treated as soft objectives. Among all grocery lists
that satisfy the hard constraints, the system prefers solutions that
maximize alignment with foods the user enjoys.

Secondary objectives, used only as tie-breakers, include minimizing
deviation from nutritional targets and maximizing nutritional value per
dollar spent.


## System Queries

The system is designed to support the following core queries:

1. Generate grocery list  
   Given a user’s dietary goal, budget, food preferences, and dietary
   restrictions, generate a grocery list that satisfies all hard
   constraints and maximizes the user preference score.

2. Evaluate alternative grocery lists  
   Given two or more candidate grocery lists that satisfy all hard
   constraints, determine which list is preferred based on the
   optimization objective.

3. Substitute food item  
   Given a food item in the grocery list and a set of user constraints,
   identify an alternative item that preserves user preference as much
   as possible while improving cost efficiency or nutritional alignment.

4. Recompute grocery list under updated constraints  
   Given a change in user inputs (e.g., budget adjustment or updated
   preferences), regenerate a grocery list that reflects the updated
   constraints while maintaining optimization priorities.


## Assumptions and Non-Goals

### Assumptions

- Nutritional values and food costs are approximate and may vary by
  brand, store, or region.
- Caloric and macronutrient targets are either provided by the user or
  computed outside the core optimization logic.
- Food availability is assumed; the system does not account for
  real-time grocery store inventory.

### Non-Goals

- Providing medical, dietary, or nutritional advice.
- Diagnosing health conditions or prescribing calorie targets.
- Guaranteeing specific health or fitness outcomes.
- Performing real-time price comparisons across grocery stores.
- Acting as a conversational or chat-based recommendation system.