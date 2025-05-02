class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        # Pass 1: Forces from the right ('R')
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Max force starting from R
            elif dominoes[i] == 'L':
                force = 0  # Force blocked by L
            elif force > 0:
                force -= 1 # Force decreases with distance
            forces[i] += force
            
        # Pass 2: Forces from the left ('L')
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n # Max force starting from L
            elif dominoes[i] == 'R':
                force = 0 # Force blocked by R
            elif force > 0:
                force -= 1 # Force decreases with distance
            forces[i] -= force # Subtract leftward force
            
        # Build result string based on net force
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
                
        return "".join(result)
