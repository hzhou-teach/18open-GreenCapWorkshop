# Brian Lu
# Need to write second half, pairing cows. :/
# Actually havent calculated sizes yet.

def main():
    N = 4
    grid = [2,3,9,3,
            4,9,9,1,
            9,9,1,7,
            2,1,1,9]
    visited = set()
    blobs = []
    blobedge = [] # Which grid indices are thouching those blobs?
    players = {} # which blobs do players own?
    #ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
    for i in range(N*N):
        if grid[i] not in visited:
            stack = []
            stack.append(i)
            visited.add(i)
            blobs.append(list())
            blobedge.append(list())
            try:
                players[grid[i]].append(len(blobs)-1)
            except KeyError:
                players[grid[i]] = []
                players[grid[i]].append(len(blobs)-1)
            #ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
            while len(stack) != 0:
                print(stack)
                hand = stack.pop()
                blobs[-1].append(hand)
                #ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
                if tileValid(N, hand, 1, 0, visited):
                    if tileFloodable(N, hand, 1, 0, grid):
                        stack.append(hand+1)
                        visited.add(hand+1)
                    else:
                        blobedge[-1].append(hand+1)
                if tileValid(N, hand, -1, 0, visited):
                    if tileFloodable(N, hand, 1, 0, grid):
                        stack.append(hand-1)
                        visited.add(hand-1)
                    else:
                        blobedge[-1].append(hand-1)
                if tileValid(N, hand, 0, 1, visited):
                    if tileFloodable(N, hand, 1, 0, grid):
                        stack.append(hand+N)
                        visited.add(hand+N)
                    else:
                        blobedge[-1].append(hand+N)
                if tileValid(N, hand, 0, -1, visited):
                    if tileFloodable(N, hand, 1, 0, grid):
                        stack.append(hand-N)
                        visited.add(hand-N)
                    else:
                        blobedge[-1].append(hand-N)
    #ヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝo(*￣▽￣*)ブヾ(≧ ▽ ≦)ゝ
    print(blobs)
    print(blobedge)
    print(players)

def tileValid(N, index, dx, dy, visited):
    x = index %N
    y = index//N
    xvalid = 0 <= (dx + x) and (dx + x) <= 3
    yvalid = 0 <= (dy + y) and (dy + y) <= 3
    if xvalid and yvalid and \
    ((x+dx)+N*(y+dy) not in visited):
        return True
    else:
        return False

def tileFloodable(N, index, dx, dy, grid):
    x = index %N
    y = index//N
    if grid[(x+dx)+N*(y+dy)] == grid[index]:
        return True
    else:
        return False
        
main()