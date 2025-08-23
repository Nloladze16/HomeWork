# Assignment 6: Grade Calculator with Functions
### Difficulty: Intermediate

Write a program with the following functions:

1. `get_letter_grade(score)` — returns letter grade (**A**, **B**, **C**, **D**, **F**) based on score  
2. `is_passing(score)` — returns `True` if score >= 60, `False` otherwise  
3. `get_grade_message(score)` — returns appropriate message based on grade

Use these functions in a **main** program that:
- Gets a score from the user
- Uses your functions to determine grade, pass/fail, and message
- Prints **all** results in a clear format

---

## Grading Scale and Messages:
```
90-100: A -> Excellent work!
80-89 : B -> Good job!
70-79 : C -> Satisfactory performance.
60-69 : D -> Needs improvement, but passing.
Below 60: F -> Failing grade. Please study harder.
```

---

## Requirements:
- Use **multiple custom functions** (at least the three above)
- Use **Boolean return values** in `is_passing`
- Practice **Pythonic return statements** (no unnecessary `if True: return True` patterns)
- Combine all functions logically in `main()`

---

## Example Runs:

### Example 1:
```
Enter your score: 95
Grade: A
Passing: Yes
Excellent work!
```

### Example 2:
```
Enter your score: 72
Grade: C
Passing: Yes
Satisfactory performance.
```

### Example 3:
```
Enter your score: 50
Grade: F
Passing: No
Failing grade. Please study harder.
```

---

**Hint:**  
`get_grade_message` should **call** `get_letter_grade` instead of duplicating the grading logic.
