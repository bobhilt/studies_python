#!/usr/bin/python
###
# Works, but fails on very large trees.  Does not pass validation tests.

class Node:
    #Track parent to make solution easy.
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val # use for dict key
        self.parent_val = None #Just the value. Avoid circular refs.
        self.level = 0

class Tree:
    #dict because we need fast access but never need to traverse.  
    tree_nodes = {}
    build_stack = []
    
    def __init__(self,h):
        n = 2**h -1

        #build perfect post-order binary tree of height h
        
        #begin with root, n.
        node = Node(n)
        node.level = h
        node.parent_val = -1
        
        self.build_stack.append(node)
        self.tree_nodes[node.val] = node
        for v in range(n-1,0,-1):
            self._add(v)

        #trying to save memory, but stack should be mostly empty by the end.
        print(len(self.build_stack))
        
    def _add(self, val):
        # because tree structure is well-defined and fully controlled until formed, 
        # modifies class variable build_stack
        node = Node(val)
        self.tree_nodes[node.val] = node
        #find spot & place it.
        placed = False
        while not placed:
            last = self.build_stack[-1] #Don't pop from stack until full

            if last.level == 1:
                #cant go lower
                self.build_stack.pop()
                
            else:
                #right first, then left or pop.
                if last.r:
                    if last.l:
                        #all full. find next one.
                        self.build_stack.pop()
                    else:
                        last.l = node.val
                        placed = True

                else:
                    last.r = node.val
                    placed = True

        node.parent_val = last.val
        node.level = last.level -1
        self.build_stack.append(node)

    def __getitem__(self,key):
        return self.tree_nodes[key]

    
    #sample from http://krenzel.org/articles/printing-trees
    #would have to be reworked with some tree descent logic.
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.r != None:
            ret += self.r.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.val)

        # Print left branch
        if self.l != None:
            ret += self.l.__str__(depth + 1)

        return ret



trees = {}

def answer(h, q):
    #MemoryError. 
    #Maybe trying to save too many large trees
    #Try eliminating cache
    
    """
    if h in trees:
        t = trees[h]
    else:
        t = Tree(h)
        trees[h] = t
    """
    t = Tree(h)
    answer = []

    for item in q:
        answer.append(t[item].parent_val)
    
    del t
    return answer

assert(answer(3,[7, 3, 5, 1]) ==  [-1, 7, 6, 3])
assert(answer(5,[19, 14, 28]) ==[21, 15, 29])