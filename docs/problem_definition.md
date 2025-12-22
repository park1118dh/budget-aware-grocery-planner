# Problem Definition

## Problem Statement

Many people want their groceries to contain foods they enjoy, help meet their dietary goals, and remain under a reasonable budget. However, developing a grocery list that meet all these constraints involves non-trivial trade-offs between cost, nutrition, and food preferences.

This system is designed to help users choose what goes in their grocery lists. Given user inputted constraints and preferences, this system creates a grocery list that prioritizes food preference, while remaining under budget, and satisfying dietary goals and restrictions.

## User Inputs

The system accepts the following user inputs:

Dietary Goal:
- Choice between: lose weight, gain muscle, or maximize nutrition
This goal influences how nutritional targets are interpreted but does not give medical advice

Budget: 
- A value that expresses the maximum price of the grocery list over a selected period of time (weekly, biweekly, or monthly)
The budget is treated as a hard constraint

Foods Enjoyed:
- The list of foods items the user enjoys or prefers
This list is treated as a soft preferences, and are prioritized during optimization when possible

Foods Disliked:
- The list of foods the user wishes to not be included in the grocery list
This is treated as a hard constraint

Dietary Restrictions: 
- Constraints, such as vegetarian, vegan, lactose free, and more, that must be respected
- Users can also choose "None" if they have no such dietary restrictions
This is treated as a hard constraint


