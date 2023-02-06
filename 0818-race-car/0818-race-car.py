class Solution:
    def racecar(self, target: int) -> int:
        seen = set()
        queue = deque([(1, 0, 0)])
        while queue:
            speed, pos, move = queue.popleft()
            if pos == target:
                return move
            
            if (pos, speed) not in seen:
                new_pos = pos + speed
                seen.add((pos, speed))
                queue.append((speed*2, new_pos, move + 1))
                
                if (new_pos < target and speed < 0) or (new_pos > target and speed > 0):
                    if speed > 0:
                        speed = -1 
                    else:
                        speed = 1 
                    queue.append((speed, pos, move + 1))
        
        return -1 