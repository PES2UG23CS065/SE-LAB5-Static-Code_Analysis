# Reflection – Static Code Analysis Lab

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were PEP8 style problems such as missing blank lines and function naming conventions. The harder ones involved handling the mutable default argument and replacing `eval()` securely, since they required understanding potential runtime side effects and security implications.

### 2. Did the static analysis tools report any false positives? If so, describe one example.
Pylint reported missing docstrings and function naming style violations, which were not true functional problems. These can be considered low-severity or false positives in the context of this simple script.

### 3. How would you integrate static analysis tools into your actual software development workflow?
Static analysis tools can be integrated into the CI/CD pipeline using GitHub Actions, so that every push or pull request automatically runs Pylint, Flake8, and Bandit. This ensures that code quality, security, and style remain consistent across the project.

### 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?
After fixing the issues, the code became more secure, readable, and maintainable. Using `with open()` improved file safety, input validation prevented crashes, replacing `eval()` removed a security risk, and structured logging made the program’s behavior easier to track and debug.
