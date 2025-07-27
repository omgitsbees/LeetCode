class Solution:
    def evaluate(self, expression: str) -> int:
        def parse_tokens(expr):
            """Parse expression into tokens, handling nested parentheses"""
            tokens = []
            i = 0
            while i < len(expr):
                if expr[i] == ' ':
                    i += 1
                elif expr[i] == '(':
                    # Find matching closing parenthesis
                    paren_count = 1
                    j = i + 1
                    while j < len(expr) and paren_count > 0:
                        if expr[j] == '(':
                            paren_count += 1
                        elif expr[j] == ')':
                            paren_count -= 1
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
                else:
                    # Parse variable or number
                    j = i
                    while j < len(expr) and expr[j] not in ' ()':
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
            return tokens
        
        def evaluate_helper(expr, scope):
            """Recursively evaluate expression with given scope"""
            expr = expr.strip()
            
            # If it's a number
            if expr.lstrip('-').isdigit():
                return int(expr)
            
            # If it's a variable
            if not expr.startswith('('):
                # Look up variable in scope (innermost first)
                for scope_dict in reversed(scope):
                    if expr in scope_dict:
                        return scope_dict[expr]
                raise ValueError(f"Variable {expr} not found")
            
            # Parse the expression
            tokens = parse_tokens(expr[1:-1])  # Remove outer parentheses
            op = tokens[0]
            
            if op == "add":
                return evaluate_helper(tokens[1], scope) + evaluate_helper(tokens[2], scope)
            
            elif op == "mult":
                return evaluate_helper(tokens[1], scope) * evaluate_helper(tokens[2], scope)
            
            elif op == "let":
                # Create new scope for this let expression
                new_scope = scope + [{}]
                
                # Process variable assignments
                i = 1
                while i < len(tokens) - 1:
                    var_name = tokens[i]
                    var_value = evaluate_helper(tokens[i + 1], new_scope)
                    new_scope[-1][var_name] = var_value
                    i += 2
                
                # Evaluate the final expression
                return evaluate_helper(tokens[-1], new_scope)
        
        return evaluate_helper(expression, [])


# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1: Simple add
    assert sol.evaluate("(add 1 2)") == 3
    
    # Test case 2: Nested operations
    assert sol.evaluate("(mult 3 (add 2 3))") == 15
    
    # Test case 3: Let with variable
    assert sol.evaluate("(let x 2 (mult x 5))") == 10
    
    # Test case 4: Let with multiple variables
    assert sol.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))") == 14
    
    # Test case 5: Nested let with shadowing
    assert sol.evaluate("(let x 3 x 2 x)") == 2
    
    # Test case 6: Complex nested expression
    # x=1, y=2, then x=(add x y)=(add 1 2)=3, finally (add x y)=(add 3 2)=5
    assert sol.evaluate("(let x 1 y 2 x (add x y) (add x y))") == 5
    
    print("All test cases passed!")

# Run tests
test_solution()
