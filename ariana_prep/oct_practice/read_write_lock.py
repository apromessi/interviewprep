# A read/write lock will allow multiple readers at a time,
# But only one writer
# No readers can read the resource when the resource is being written, and
# No writers can write the resource when it is being read.
# Interface:
# RWLock:
#     acquireReadLock() - blocks
#     releaseReadLock()
#     acquireWriteLock() - blocks
#     releaseWriteLock()
# 
# In order to implement this feature, we’ll need the lock primitive.

#ideas:
# 1. locks can copy resource to ensure that they return the correct version. 
# 2. lock removes resource from source collection and adds it back once released
# 3. key/value store to keep track of which resources are locked - lock api can do a 'permissions' check

#Just one integer

# acquire lock -> block resource -> confirmation -> perform operation -> confirmation -> release resource

"""
Lock:
    acquire()
    release()

"""

class Lock(object):
    def __init__(self, is_locked=False):
        self.is_locked = is_locked
    
    def acquire(self):
        if self.is_locked:
            raise Exception

        self.is_locked = True
    
    def release(self):
        self.is_locked = False


[int, Lock()]

class RWLock(object):
    def __init__(self, value):
        self.value = value
        self.write_lock = Lock()
        self.read_lock = Lock()

    def acquireReadLock(self):
        if self.write_lock.is_locked:
            raise Exception # write locked already
        try:
            self.read_lock.acquire()
        except Exception:
            raise Exception # with message

    def releaseReadLock(self):
        self.lock.release()

    def acquireWriteLock(self):
        try:
            self.lock.acquire()
        except Exception:
            raise Exception # with message

    def releaseWriteLock(self):
        self.lock.release()
    
    def block(self):
        pass