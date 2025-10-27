# Static Code Analysis – Inventory System

## Objective
The goal of this exercise is to perform static code analysis on the `inventory_system.py` script using tools such as **Pylint**, **Bandit**, and **Flake8**.  
The process identifies potential security risks, code quality issues, and violations of Python’s best practices.  
After detecting issues, fixes were implemented and verified by re-running the tools.

---

## Tools Used
- **Pylint** – for coding style and logic warnings  
- **Flake8** – for PEP8 compliance and formatting  
- **Bandit** – for security vulnerability detection  

---

## Issues and Fixes Summary

| Issue | Tool | Line(s) | Description | Fix Approach |
|--------|------|----------|--------------|---------------|
| Dangerous use of `eval()` | Bandit | 59 | `eval()` is unsafe and can execute arbitrary code | Replaced with `ast.literal_eval()` for safe evaluation |
| Bare `except:` used | Pylint / Bandit / Flake8 | 19 | Generic exception hides real errors | Replaced with `except Exception as e:` and logged error message |
| Mutable default argument (`logs=[]`) | Pylint | 8 | Same list shared across calls | Changed default to `None` and initialized within function |
| File handling without encoding / `with` | Pylint | 26, 32 | Missing encoding & manual open/close | Used `with open(file, encoding='utf-8')` for safe file handling |
| Input validation missing | Manual | 8, 14 | No type checking for user inputs | Added type checks for `item` (str) and `qty` (int/float) |
| Missing logging configuration | Manual | Main block | No logging setup | Configured logging with timestamps and severity levels |
| Missing docstrings | Pylint | Multiple | Functions lacked descriptions | Added descriptive docstrings |
| Non-snake_case function names | Pylint | Multiple | Function naming style | Renamed to snake_case for PEP8 compliance |

---

## Results After Fixes
After applying the fixes and re-running static analysis tools:
- The **Pylint score** improved significantly (close to 10/10).  
- **Bandit** reported no remaining high or medium severity security issues.  
- **Flake8** showed clean results with proper formatting and spacing.  

---

## Outcome
This task improved code security, readability, and maintainability.  
The refactored version of `inventory_system.py` follows **PEP8 standards**, includes **safe coding practices**, and eliminates **previous security and logic issues**.

---

**Author:** Ananya Shet  
**Course:** Software Engineering Lab – Static Code Analysis  
**Date:** October 2025
