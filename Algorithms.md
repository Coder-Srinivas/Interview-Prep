# Coding Cheat Sheet

- **Array & String**  
  - Boyer-Moore Majority Vote  
  - Merge Sort (with inversion count)  
  - Rabin-Karp

- **Math**
  - Evaluate Postfix/Reverse Polish Expression
  - Convert Infix to Postfix
  - Build an Expression Tree
  - Evaluate an Expression

- **Trie**
  - Add to trie
  - Erase from trie
  - Check if a word exists
  - Check if a prefix exits

- **Graph**  
  - Union-Find (Disjoint Set) / Kruskal’s  
  - Prim’s Algorithm  
  - Dijkstra’s Algorithm  
  - Floyd-Warshall Algorithm  
  - Kosaraju’s Algorithm (SCC)  
  - Check cycle in a directed graph  
  - Check if a graph is bipartite  
  - BFS (Breadth First Search)  
  - DFS (Depth First Search)

- **Design**  
  - LRU Cache  
  - LFU Cache  

---

## 1. Array & String

### Boyer-Moore Majority Vote

```python
def majorityElement(nums: List[int]) -> List[int]:
    majority1 = majority2 = 0
    count1 = count2 = 0

    for num in nums:
        if num == majority1:
            count1 += 1
        elif num == majority2:
            count2 += 1
        elif count1 == 0:
            majority1 = num
            count1 = 1
        elif count2 == 0:
            majority2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Verify that majority1 and majority2 appear more than len(nums) // 3 times.
    count1 = count2 = 0
    for num in nums:
        if num == majority1:
            count1 += 1
        elif num == majority2:
            count2 += 1

    res = []
    if count1 > len(nums) // 3:
        res.append(majority1)
    if count2 > len(nums) // 3:
        res.append(majority2)

    return res
```

### Merge Sort with inversion count

```python
def merge_sort(arr, left, right):
    c = 0
    if left < right:
        mid = (left + right) // 2
        c += merge_sort(arr, left, mid)
        c += merge_sort(arr, mid + 1, right)
        c += merge(arr, left, mid, right)
    return c

def merge(arr, left, mid, right):
    temp = []
    k = 0
    l = left
    m = mid + 1
    r = right
    count = 0

    while l <= mid and m <= right:
        if arr[l] <= arr[m]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[m])
            count += (mid - l + 1)
            m += 1
        k += 1

    while l <= mid:
        temp.append(arr[l])
        l += 1
        k += 1

    while m <= right:
        temp.append(arr[m])
        m += 1
        k += 1

    k = 0
    while left <= right:
        arr[left] = temp[k]
        left += 1
        k += 1

    return count

```

### Rabin Karp

```
def rabin_karp(search: str, target: str) -> bool:
    base = 1000000007
    target_code = 0
    current_code = 0
    n = len(target)
    power = [1]
    
    # Precompute powers of 31
    for _ in range(len(search)):
        power.append((power[-1] * 31) % base)

    # Compute hash code for `target` and first `n` characters of `search`
    for i, c in enumerate(target):
        c2 = search[i]
        target_code = (target_code * 31 + (27 ** ord(c))) % base
        current_code = (current_code * 31 + (27 ** ord(c2))) % base

    if current_code == target_code and search[:n] == target:
        return True

    for i in range(n, len(search)):
        c = search[i]
        prev = search[i - n]

        current_code = (
            31 * (current_code - power[n - 1] * (27 ** ord(prev))) + (27 ** ord(c))
        ) % base

        if current_code == target_code and search[i - n + 1 : i + 1] == target:
            return True

    return False

```

## Math

### Evaluate Reverse Polish Notation

```python
def evalRPN(self, tokens: List[str]) -> int:    
    stack = []
    i = 0
    operators = ['+', '-', '/', '*']

    while i < len(tokens):
        token = tokens[i]
        if token in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            total = 0
            if token == '+':
                total = num1 + num2
            elif token == '-':
                total = num1 - num2
            elif token == '*':
                total = num1 * num2
            else:
                total = int(num1 / num2)
            
            stack.append(total)
        else:
            stack.append(int(token))
        
        i += 1
    
    return stack[0]
```

### Construct Reverse Polish Notation

```python
def getNumber(s, idx):
    num = []
    while idx < len(s):
        if s[idx].isdigit():
            num.append(s[idx])
        else:
            break
        idx += 1
    
    return int("".join(num)), idx
        
def constructReversePolish(s):
    s = s.replace(' ', '')
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -1}
    stack = []
    ans = []
    idx = 0
    
    while idx < len(s):
        if s[idx] == ' ':
            idx += 1
            continue
        if s[idx].isdigit():
            num, idx = getNumber(s, idx)
            ans.append(num)
            continue
        elif s[idx] == '(':
            stack.append('(')
        elif s[idx] == ')':
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[s[idx]]:
                ans.append(stack.pop())
            
            # Checking if it's a unary operator
            if s[idx] == '-' and idx-1 < 0 or s[idx-1] == '(' or s[idx-1] in precedence.keys():
                ans.append(0)
            stack.append(s[idx])
        idx += 1
    while stack:
        ans.append(stack.pop())
    return ans
```

### Construt an Expression Tree

```python
def expTree(self, s: str) -> 'Node':

    def getNumber(s, idx):
        num = []
        while idx < len(s):
            if s[idx].isdigit():
                num.append(s[idx])
            else:
                break
            idx += 1
        
        return int("".join(num)), idx
    def constructReversePolish(s):
        s = s.replace(' ', '')
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -1}
        stack = []
        ans = []
        idx = 0
        
        while idx < len(s):
            if s[idx] == ' ':
                idx += 1
                continue
            if s[idx].isdigit():
                num, idx = getNumber(s, idx)
                ans.append(num)
                continue
            elif s[idx] == '(':
                stack.append('(')
            elif s[idx] == ')':
                while stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence[stack[-1]] >= precedence[s[idx]]:
                    ans.append(stack.pop())
                
                # Checking if it's a unary operator
                if s[idx] == '-' and idx-1 < 0 or s[idx-1] == '(' or s[idx-1] in precedence.keys():
                    ans.append(0)
                stack.append(s[idx])
            idx += 1
        while stack:
            ans.append(stack.pop())
        return ans

    reversePolish = constructReversePolish(s)
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in reversePolish:
        node = None
        if token in operators:
            right = stack.pop()
            left = stack.pop()
            node = Node(token, left, right)
        else:
            node = Node(str(token))
        
        stack.append(node)
    
    return stack[0]
```

### Evaluate an Expression

```python
def calculate(self, s: str) -> int:
    def getNumber(s, idx):
        num = []
        while idx < len(s):
            if s[idx].isdigit():
                num.append(s[idx])
            else:
                break
            idx += 1
        
        return int("".join(num)), idx

    def constructReversePolish(s):
        s = s.replace(' ', '')
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -1}
        stack = []
        ans = []
        idx = 0
        
        while idx < len(s):
            if s[idx] == ' ':
                idx += 1
                continue
            if s[idx].isdigit():
                num, idx = getNumber(s, idx)
                ans.append(num)
                continue
            elif s[idx] == '(':
                stack.append('(')
            elif s[idx] == ')':
                while stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence[stack[-1]] >= precedence[s[idx]]:
                    ans.append(stack.pop())
                
                # Checking if it's a unary operator
                if s[idx] == '-' and idx-1 < 0 or s[idx-1] == '(' or s[idx-1] in precedence.keys():
                    ans.append(0)
                stack.append(s[idx])
            idx += 1
        while stack:
            ans.append(stack.pop())
        return ans

    def evalRPN(tokens: List[str]) -> int:
        stack = []
        i = 0
        operators = ['+', '-', '/', '*']

        while i < len(tokens):
            token = tokens[i]
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop() if stack else 0
                total = 0
                if token == '+':
                    total = num1 + num2
                elif token == '-':
                    total = num1 - num2
                elif token == '*':
                    total = num1 * num2
                else:
                    total = int(num1 / num2)
                
                stack.append(total)
            else:
                stack.append(token)
            
            i += 1
        return stack[0]
    reversePolish = constructReversePolish(s)
    return evalRPN(reversePolish)
```
## Trie


```python
class Trie:
    def __init__(self):
        self.m = {}

    def insert(self, word: str) -> None:
        temp = self.m
        for i in range(len(word) - 1):
            c = word[i]
            if c not in temp:
                temp[c] = (0, {})
            temp = temp[c][1]

        if word[-1] not in temp:
            temp[word[-1]] = (1, {})
        else:
            prev = temp[word[-1]]
            temp[word[-1]] = (prev[0] + 1, prev[1])

    def countWordsEqualTo(self, word: str) -> int:
        temp = self.m
        for i in range(len(word) - 1):
            c = word[i]
            if c not in temp:
                return 0
            temp = temp[c][1]
        if word[-1] not in temp:
            return 0
        return temp[word[-1]][0]

    def countWordsStartingWith(self, prefix: str) -> int:
        temp = self.m
        for i in range(len(prefix) - 1):
            c = prefix[i]
            if c not in temp:
                return 0
            temp = temp[c][1]
        if prefix[-1] not in temp:
            return 0

        current = temp[prefix[-1]]
        return current[0] + self.getAllWords(current[1])

    def getAllWords(self, d: dict) -> int:
        ans = 0
        for key in d.keys():
            ans += d[key][0] + self.getAllWords(d[key][1])
        return ans

    def erase(self, word: str) -> None:
        temp = self.m
        for i in range(len(word) - 1):
            c = word[i]
            temp = temp[c][1]
        prev = temp[word[-1]]
        temp[word[-1]] = (prev[0] - 1, prev[1])
```

## 3. Graph

### Union Find

```python
parent = [x for x in range(len(points))]
rank = [1] * len(points)

def find(node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return parent[node]

def union(u, v):
    p1 = find(u)
    p2 = find(v)

    if p1 == p2:
        return False

    if rank[p1] >= rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
    else:
        parent[p1] = p2
        rank[p2] += rank[p1]
    return True

```

### Prims

```python
import heapq

def prims(adj):
    """
    :param adj: adjacency list -> { u: [(dist, v), (dist, w), ...] }
    """
    heap = [(0, 0)]
    cost = 0
    visited = set()
    while len(visited) < len(adj):
        dist, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        cost += dist

        for d, n in adj[u]:
            if n not in visited:
                heapq.heappush(heap, (d, n))

    return cost
```

### Dijkstra

```python
from collections import defaultdict
import heapq

def dijkstra(times, n, k):
    """
    :param times: list of edges (u, v, w) meaning u->v with weight w
    :param n: total number of nodes
    :param k: starting node
    """
    dist = [float('inf')] * (n + 1)
    dist[k] = 0

    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    heap = [(0, k)]
    visited = set()

    while heap:
        curr_dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                if curr_dist + weight < dist[neighbor]:
                    dist[neighbor] = curr_dist + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))

    return dist
```

### Floyd Warshall

```python
def floyd_warshall(dist, V):
    """
    :param dist: adjacency matrix for the graph (dist[u][v] = weight of edge u->v)
    :param V: number of vertices
    """
    for via in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
```

### Kosaraju Algorithm

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(v)

    def _transpose(self):
        transposed_graph = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def _fill_order(self, visited, stack):
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)

    def _dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited, component)

    def kosaraju_scc(self):
        stack = deque()
        visited = [False] * self.V

        # Fill nodes in stack according to finishing times
        self._fill_order(visited, stack)

        # Create a transposed graph
        transposed_graph = self._transpose()

        visited = [False] * self.V
        scc_list = []

        # Process nodes in order defined by Stack
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph._dfs_util(node, visited, component)
                scc_list.append(component)

        return scc_list
```

### Check Cycle in a Directed Graph

```python
from collections import defaultdict

adj = defaultdict(set)
for u, v in edges:
    adj[u].add(v)

visited = set()

def check_cycle(u):
    # If u is visited and has outgoing edges, a cycle is found
    if u in visited and len(adj[u]) != 0:
        return True
    visited.add(u)
    for n in adj[u]:
        if check_cycle(n):
            return True
    adj[u] = set()  # remove edges once visited
    return False
```

### Bipartite Check

```python
from collections import defaultdict

def is_bipartite(graph):
    vis = defaultdict(int)

    def dfs(i, color):
        if i in vis:
            return vis[i] == color
        vis[i] = color
        for n in graph[i]:
            if not dfs(n, (color + 1) % 2):
                return False
        return True

    for i in range(len(graph)):
        if i not in vis:
            if not dfs(i, 1):
                return False
    return True
```

### BFS

```python
from collections import deque

def bfs(graph, start):
    """
    :param graph: adjacency list representation -> { node: [neighbors...] }
    :param start: starting node
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
```

### DFS

```python
def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result

```

## 4. Design

## LRU Cache

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        return len(self.map)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        val = self.map[key].val
        self.put(key, val)
        return val

    def insertAtHead(self, key, value, node=None):
        if not node:
            node = Node(key, value)
            self.map[key] = node
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def deleteAtTail(self):
        deleted = self.tail.prev
        prev_node = deleted.prev
        self.tail.prev = prev_node
        prev_node.next = self.tail
        del self.map[deleted.key]
        return deleted

    def deleteNode(self, key):
        if key not in self.map:
            return
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.map[key]
        return node

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            self.insertAtHead(key, value)
        else:
            node = self.map[key]
            node.val = value
            # Move to head
            node.prev.next = node.next
            node.next.prev = node.prev
            self.insertAtHead(key, value, node)

        if len(self.map) > self.capacity:
            self.deleteAtTail()
```

### LFU Cache

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def size(self):
        return len(self.map)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        val = self.map[key].val
        self.put(key, val)
        return val

    def insertAtHead(self, key, value, node=None):
        if not node:
            node = Node(key, value)
            self.map[key] = node
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node
    
    def deleteAtTail(self):
        deleted = self.tail.prev
        prev_node = deleted.prev
        self.tail.prev = prev_node
        prev_node.next = self.tail
        del self.map[deleted.key]
        return deleted
    
    def deleteNode(self, key):
        if key not in self.map:
            return
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.map[key]
        return node

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            self.insertAtHead(key, value)
        else:
            node = self.map[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self.insertAtHead(key, value, node)
        
        if len(self.map) > self.capacity:
            self.deleteAtTail()

class LFUCache:
    def __init__(self, capacity: int):
        self.freq = {}
        self.map = {}
        self.capacity = capacity
        self.leastFrequency = 0

    def get(self, key: int) -> int:
        if key not in self.freq:
            return -1
        keyFreq = self.freq[key]
        lru = self.map[keyFreq]
        val = lru.get(key)
        return self.put(key, val)
        
    def updateFrequency(self, key, val, keyFreq):
        if keyFreq not in self.map:
            self.map[keyFreq] = LRUCache(10000000)
        self.map[keyFreq].put(key, val)
    
    def deleteLeastFrequency(self):
        lru = self.map[self.leastFrequency]
        node = lru.deleteAtTail()
        del self.freq[node.key]

    def put(self, key: int, value: int) -> int:
        if self.capacity == 0:
            return -1

        # If the key is new
        if key not in self.freq:
            if len(self.freq) == self.capacity:
                self.deleteLeastFrequency()
            self.freq[key] = 1
            self.leastFrequency = 1
            if 1 not in self.map:
                self.map[1] = LRUCache(100000000)
            self.map[1].put(key, value)
            return value
        
        # If the key already exists
        keyFreq = self.freq[key]
        lru = self.map[keyFreq]
        lru.deleteNode(key)

        self.updateFrequency(key, value, keyFreq + 1)

        if keyFreq == self.leastFrequency and lru.size() == 0:
            self.leastFrequency += 1

        self.freq[key] += 1
        return value
```