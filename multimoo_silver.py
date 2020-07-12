# Brian Lu

def main():
    N = 4
    grid = [2,3,9,3,
            4,9,9,1,
            9,9,1,7,
            2,1,1,9]
    visited = set()
    blobs = []
    players = {} # which blobs do players own?

    for i in range(N*N):
        if grid[i] not in visited:
            stack = []
            stack.append(i)
            visited.add(i)
            blobs.append(list())
            try:
                players[grid[i]].append(len(blobs)-1)
            except KeyError:
                players[grid[i]] = []
                players[grid[i]].append(len(blobs)-1)
            while len(stack) != 0:
                print(stack)
                hand = stack.pop()
                blobs[-1].append(hand)
                if tileValid(N, hand, 1, 0, visited, grid):
                    stack.append(hand+1)
                    visited.add(hand+1)
                if tileValid(N, hand, -1, 0, visited, grid):
                    stack.append(hand-1)
                    visited.add(hand-1)
                if tileValid(N, hand, 0, 1, visited, grid):
                    stack.append(hand+N)
                    visited.add(hand+N)
                if tileValid(N, hand, 0, -1, visited, grid):
                    stack.append(hand-N)
                    visited.add(hand-N)

    print(blobs)
    print(players)

def tileValid(N, index, dx, dy, visited, grid):
    x = index %N
    y = index//N
    xvalid = 0 <= (dx + x) and (dx + x) <= 3
    yvalid = 0 <= (dy + y) and (dy + y) <= 3
    if xvalid and yvalid and \
    ((x+dx)+N*(y+dy) not in visited) and \
    grid[(x+dx)+N*(y+dy)] == grid[index]:
        return True
    else:
        return False
main()