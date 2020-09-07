import threading
'''
class PurchaseRequest:

    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._lock = threading,Lock()

    def incr(self, delta = 1):
        # self._lock.acquire()
        # self._value += delta
        # self._lock.release

        with self._lock:
            self.value += delta


    def decr(self, delta = 1):
        # self._lock.acquire()
        # self._value -= delta
        # self._lock.release()

        with self._lock:
            self._value -= delta
'''
class PurchaseRequest:

    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._lock = threading,RLock()

    def incr(self, delta = 1):
        # self._lock.acquire()
        # self._value += delta
        # self._lock.release

        with self._lock:
            self.value += delta


    def decr(self, delta = 1):
        # self._lock.acquire()
        # self._value -= delta
        # self._lock.release()

        with self._lock:
            incr(-delta)










