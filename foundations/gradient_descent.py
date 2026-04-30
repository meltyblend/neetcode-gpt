class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal place

        x = init
        a = learning_rate

        for i in range(iterations):
            x_new = x - a * 2 * x
            x = x_new
        
        return round(x, 5)
        
        pass