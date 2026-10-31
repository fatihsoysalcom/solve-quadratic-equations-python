import math
import cmath # For complex numbers

def solve_quadratic_equation(a, b, c):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.
    Handles real and complex roots.
    """
    print(f"\nSolving: {a}x^2 + {b}x + {c} = 0")

    if a == 0:
        # As per the article, a quadratic equation requires a != 0.
        # If a is 0, it becomes a linear equation or a degenerate case.
        # Makaleye göre, karesel bir denklem için a ≠ 0 olmalıdır.
        # Eğer a sıfırsa, denklem doğrusal hale gelir veya dejenere bir durum olur.
        if b == 0:
            if c == 0:
                return "This is a degenerate case (0=0), infinite solutions."
            else:
                return "This is a degenerate case (c!=0, 0=0), no solution."
        else:
            x = -c / b
            return f"This is a linear equation (a=0). One root: x = {x}"

    # Calculate the discriminant (delta)
    # Diskriminant (delta) hesaplanır
    delta = (b**2) - 4*(a*c)

    print(f"Discriminant (delta): {delta}")

    # Determine the nature of the roots based on the discriminant
    # Diskriminanta göre köklerin doğası belirlenir
    if delta > 0:
        # Two distinct real roots
        # İki farklı gerçek kök
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return f"Two distinct real roots: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        # One real root (repeated)
        # Bir gerçek kök (çift katlı)
        x = -b / (2*a)
        return f"One real root (repeated): x = {x}"
    else:
        # Two complex roots
        # İki karmaşık kök
        # Using cmath for complex square root
        x1 = (-b - cmath.sqrt(delta)) / (2*a)
        x2 = (-b + cmath.sqrt(delta)) / (2*a)
        return f"Two complex roots: x1 = {x1}, x2 = {x2}"

# --- Example Usage ---
print("--- Quadratic Equation Solver ---")

# Case 1: Two distinct real roots (delta > 0)
# Örnek 1: İki farklı gerçek kök (delta > 0)
print(solve_quadratic_equation(1, -3, 2)) # x^2 - 3x + 2 = 0  => (x-1)(x-2) = 0 => x=1, x=2

# Case 2: One real root (repeated) (delta = 0)
# Örnek 2: Bir gerçek kök (çift katlı) (delta = 0)
print(solve_quadratic_equation(1, -4, 4)) # x^2 - 4x + 4 = 0  => (x-2)^2 = 0 => x=2

# Case 3: Two complex roots (delta < 0)
# Örnek 3: İki karmaşık kök (delta < 0)
print(solve_quadratic_equation(1, 2, 5)) # x^2 + 2x + 5 = 0 => delta = 4 - 20 = -16

# Case 4: Another example with real roots
print(solve_quadratic_equation(2, 5, -3)) # 2x^2 + 5x - 3 = 0 => delta = 25 - 4(2)(-3) = 25 + 24 = 49

# Case 5: Example of a linear equation (a=0) - handled as per article's definition
# Örnek 5: Doğrusal denklem örneği (a=0) - makalenin tanımına göre ele alınmıştır
print(solve_quadratic_equation(0, 2, 4)) # 2x + 4 = 0 => x = -2

# Case 6: Degenerate cases (a=0, b=0)
# Örnek 6: Dejenere durumlar (a=0, b=0)
print(solve_quadratic_equation(0, 0, 5)) # 5 = 0 => No solution
print(solve_quadratic_equation(0, 0, 0)) # 0 = 0 => Infinite solutions
