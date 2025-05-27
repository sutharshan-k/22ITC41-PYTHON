class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = 0
        while True:
            if x >= 1 and y >= 4:
                x -= 1
                y -= 4
            else:
                return "Bob" if turn % 2 == 0 else "Alice"
            turn += 1
