Back to [Modules overview](https://github.com/pyrustic/probed/blob/master/docs/modules/README.md)
  
# Module documentation
>## probed.\_\_init\_\_
No description
<br>
[classes (4)](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed.__init__/classes.md)


## Classes
```python
class Info(object):
    """
    This class contains data that describe a change event.
    Three attributes are always available:
    
    - collection: the collection object, i.e. an instance of probed.ProbedDict,
    probed.ProbedList or probed.ProbedSet
    
    - container: a string that indicates the type of container.
    The containers are 'dict', 'list' and 'set'.
    
    - operation: a string that indicates the type of operation.
    The operations are same as the names of the methods (minus underscores)
    of the collections.
    Example, these are the operations for probed.ProbedDict:
    'pop', 'setdefault', 'clear', 'popitem', 'update', 'delitem', 'setitem'
    
    Then there are attributes that are available or not, depending of the operation
    and the type of container.
    Example: when you append a value to an instance of probed.ProbedList,
    the operation name is "append", the container is "list", the collection is
    the actual instance of probed.ProbedList, and then you have an extra attribute
    called 'value'. This attribute contains the value that will be added to
    the collection.
    Note: the extra attributes mimic the name of the parameters of the operation method.
    
    Illustration:
    
    def on_change(info):
        info.container # 'dict'
        info.collection # the actual plist object
        info.operation # 'append'
        info.value # 'hello'
    
    plist = probed.ProbedList(on_change=on_change)
    plist.append("hello") # the name of the parameter of this operation is 'value'
    """

    def __init__(self, collection, container, operation, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def collection(self):
        """
        
        """

    @property
    def container(self):
        """
        
        """

    @property
    def operation(self):
        """
        
        """

```

```python
class ProbedDict(dict):
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def __init__(self, items=None, probe=None, on_change=None):
        """
        - items: default value of the collection
        
        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Info.
        It should return the same instance (edited or not) of probed.Info
        it got as argument, or return None to cancel the change operation.
        
        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Info.
        """

    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """

    @changed.setter
    def changed(self, val):
        """
        
        """

    @property
    def on_change(self):
        """
        
        """

    @on_change.setter
    def on_change(self, val):
        """
        
        """

    @property
    def probe(self):
        """
        
        """

    @probe.setter
    def probe(self, val):
        """
        
        """

    def clear(self):
        """
        D.clear() -> None.  Remove all items from D.
        """

    # inherited from dict
    def fromkeys(type, iterable, value=None, /):
        """
        Create a new dictionary with keys from iterable and values set to value.
        """

    # inherited from dict
    def get(self, key, default=None, /):
        """
        Return the value for key if key is in the dictionary, else default.
        """

    def pop(self, key, default=None):
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """

    def popitem(self):
        """
        Remove and return a (key, value) pair as a 2-tuple.
        
        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """

    def setdefault(self, key, default=None):
        """
        Insert key with a value of default if key is not in the dictionary.
        
        Return the value for key if key is in the dictionary, else default.
        """

    def update(self, other=None, **kwargs):
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """

```

```python
class ProbedList(list):
    """
    Built-in mutable sequence.
    
    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    """

    def __init__(self, items=None, probe=None, on_change=None):
        """
        - items: default value of the collection
        
        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Info.
        It should return the same instance (edited or not) of probed.Info
        it got as argument, or return None to cancel the change operation.
        
        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Info.
        """

    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """

    @changed.setter
    def changed(self, val):
        """
        
        """

    @property
    def on_change(self):
        """
        
        """

    @on_change.setter
    def on_change(self, val):
        """
        
        """

    @property
    def probe(self):
        """
        
        """

    @probe.setter
    def probe(self, val):
        """
        
        """

    def append(self, value):
        """
        Append object to the end of the list.
        """

    def clear(self):
        """
        Remove all items from list.
        """

    # inherited from list
    def copy(self, /):
        """
        Return a shallow copy of the list.
        """

    # inherited from list
    def count(self, value, /):
        """
        Return number of occurrences of value.
        """

    def extend(self, value):
        """
        Extend list by appending elements from the iterable.
        """

    # inherited from list
    def index(self, value, start=0, stop=9223372036854775807, /):
        """
        Return first index of value.
        
        Raises ValueError if the value is not present.
        """

    def insert(self, index, value):
        """
        Insert object before index.
        """

    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        
        Raises IndexError if list is empty or index is out of range.
        """

    def remove(self, value):
        """
        Remove first occurrence of value.
        
        Raises ValueError if the value is not present.
        """

    def reverse(self):
        """
        Reverse *IN PLACE*.
        """

    def sort(self, *, key=None, reverse=False):
        """
        Sort the list in ascending order and return None.
        
        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).
        
        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
        
        The reverse flag can be set to sort in descending order.
        """

```

```python
class ProbedSet(set):
    """
    set() -> new empty set object
    set(iterable) -> new set object
    
    Build an unordered collection of unique elements.
    """

    def __init__(self, items=None, probe=None, on_change=None):
        """
        - items: default value of the collection
        
        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Info.
        It should return the same instance (edited or not) of probed.Info
        it got as argument, or return None to cancel the change operation.
        
        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Info.
        """

    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """

    @changed.setter
    def changed(self, val):
        """
        
        """

    @property
    def on_change(self):
        """
        
        """

    @on_change.setter
    def on_change(self, val):
        """
        
        """

    @property
    def probe(self):
        """
        
        """

    @probe.setter
    def probe(self, val):
        """
        
        """

    def add(self, item):
        """
        Add an element to a set.
        
        This has no effect if the element is already present.
        """

    def clear(self):
        """
        Remove all elements from this set.
        """

    def difference_update(self, *others):
        """
        Remove all elements of another set from this set.
        """

    def discard(self, item):
        """
        Remove an element from a set if it is a member.
        
        If the element is not a member, do nothing.
        """

    def intersection_update(self, *others):
        """
        Update a set with the intersection of itself and another.
        """

    def pop(self):
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """

    def remove(self, item):
        """
        Remove an element from a set; it must be a member.
        
        If the element is not a member, raise a KeyError.
        """

    def symmetric_difference_update(self, other):
        """
        Update a set with the symmetric difference of itself and another.
        """

    def update(self, *others):
        """
        Update a set with the union of itself and others.
        """

```

