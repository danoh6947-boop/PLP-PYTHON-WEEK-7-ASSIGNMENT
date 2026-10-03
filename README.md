# Week 7 Assignment - Shopping List Manager

## Files

- `list_warmup.py` - Demonstrates creating a list, accessing items by index, using append and remove, and counting items with len().
- `shopping_list.py` - Provides a menu-based shopping list manager for adding, removing, showing, and finishing a shopping list.
- `list_report.py` - Loops through a shopping list to number items, count names with more than four letters, and find the longest item.
- `screenshots/` - Contains screenshots showing each Python program running.

## Why is it safer to check in before calling .remove()?

Checking with `in` before calling `.remove()` is safer because `.remove()` causes a ValueError if the item is not in the list. The check allows the program to print a helpful message instead of crashing.