class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._cap = capacity
        self._cache = {}
        self._tail = None
        self._head = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        n = self._cache[key]
        pre, nex = n.prev, n.next
        if pre:
            pre.next = nex
            if nex:
                nex.prev = pre
            else:
                self._tail = pre
            n.next = self._head
            self._head = n
            n.pre = None
        return n.k

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        n = Node(key, value)
        if self._head:
            n.next = self._head
            self._head.prev = n
        self._head = n
        if not self._tail:
            self._tail = n
        self._cache[key] = n
        if len(self._cache) > self._cap:
            k = self._tail.k
            self._tail = self._tail.prev
            self._tail.next = None
            del self._cache[k]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
