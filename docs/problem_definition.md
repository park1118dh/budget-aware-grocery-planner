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


