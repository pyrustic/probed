class ProbedDict(dict):
    """Definition of the class to make probed dicts"""
    def __init__(self, items=None, probe=None,
                 on_change=None):
        """
        Init.

        [parameters]
        - items: default value of the collection
        
        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Context.
        It should return the same instance (edited or not) of probed.Context
        it got as argument, or return None to cancel the change operation.
        
        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Context.
        
        """
        super().__init__(items if items else {})
        self.__probe = probe
        self.__on_change = on_change
        self.__changed = False

    @property
    def probe(self):
        return self.__probe

    @probe.setter
    def probe(self, val):
        self.__probe = val

    @property
    def on_change(self):
        return self.__on_change

    @on_change.setter
    def on_change(self, val):
        self.__on_change = val

    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """
        return self.__changed

    @changed.setter
    def changed(self, val):
        self.__changed = val

    def clear(self):
        context = self.__get_context("clear")
        context = self.__run_probe(context)
        if not context:
            return
        val = super().clear()
        self.__changed = True
        self.__run_on_change(context)
        return val

    def pop(self, key, default=None):
        context = self.__get_context("pop", key=key,
                               default=default)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().pop(context.key, context.default)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def popitem(self):
        context = self.__get_context("popitem")
        context = self.__run_probe(context)
        if not context:
            return
        val = super().popitem()
        self.__changed = True
        self.__run_on_change(context)
        return val

    def setdefault(self, key, default=None):
        context = self.__get_context("setdefault", key=key,
                               default=default)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().setdefault(context.key, context.default)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def update(self, other=None, **kwargs):
        other = self.__merge_update_other_kwargs(other,
                                                 **kwargs)
        context = self.__get_context("update", other=other)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().update(other)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __delitem__(self, key):
        context = self.__get_context("delitem", key=key)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__delitem__(context.key)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __setitem__(self, key, value):
        context = self.__get_context("setitem", key=key,
                               value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__setitem__(context.key, context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __merge_update_other_kwargs(self, other, **kwargs):
        if not other:
            other = {}
        if not isinstance(other, dict):
            cache = {}
            for key, value in other:
                cache[key] = value
            other = cache
        for key, value in kwargs:
            other[key] = value
        return other

    def __get_context(self, operation, **kwargs):
        return Context(self, "dict", operation, **kwargs)

    def __run_probe(self, context):
        if self.__probe:
            context = self.__probe(context)
        return context

    def __run_on_change(self, context):
        if self.__on_change:
            self.__on_change(context)


class ProbedList(list):
    """Definition of the class to make probed lists"""
    def __init__(self, items=None, probe=None,
                 on_change=None):
        """
        Init.

        [parameters]
        - items: default value of the collection

        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Context.
        It should return the same instance (edited or not) of probed.Context
        it got as argument, or return None to cancel the change operation.

        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Context.

        """
        super().__init__(items if items else ())
        self.__probe = probe
        self.__on_change = on_change
        self.__changed = False

    @property
    def probe(self):
        return self.__probe

    @probe.setter
    def probe(self, val):
        self.__probe = val

    @property
    def on_change(self):
        return self.__on_change

    @on_change.setter
    def on_change(self, val):
        self.__on_change = val

    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """
        return self.__changed

    @changed.setter
    def changed(self, val):
        self.__changed = val

    def append(self, value):
        context = self.__get_context("append", value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().append(context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def clear(self):
        context = self.__get_context("clear")
        context = self.__run_probe(context)
        if not context:
            return
        val = super().clear()
        self.__changed = True
        self.__run_on_change(context)
        return val

    def extend(self, value):
        context = self.__get_context("extend", value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().extend(context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def insert(self, index, value):
        context = self.__get_context("insert", index=index,
                               value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().insert(context.index, context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def pop(self, index=-1):
        context = self.__get_context("pop", index=index)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().pop(context.index)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def remove(self, value):
        context = self.__get_context("remove", value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().remove(context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def reverse(self):
        context = self.__get_context("reverse")
        context = self.__run_probe(context)
        if not context:
            return
        val = super().reverse()
        self.__changed = True
        self.__run_on_change(context)
        return val

    def sort(self, *, key=None, reverse=False):
        context = self.__get_context("sort", key=key,
                               reverse=reverse)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().sort(key=context.key, reverse=context.reverse)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __delitem__(self, index):
        context = self.__get_context("delitem", index=index)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__delitem__(context.index)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __iadd__(self, value):
        context = self.__get_context("iadd", value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__iadd__(context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __imul__(self, value):
        context = self.__get_context("imul", value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__imul__(context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __setitem__(self, index, value):
        context = self.__get_context("setitem", index=index,
                               value=value)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__setitem__(context.index, context.value)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __get_context(self, operation, **kwargs):
        return Context(self, "list", operation, **kwargs)

    def __run_probe(self, context):
        if self.__probe:
            context = self.__probe(context)
        return context

    def __run_on_change(self, context):
        if self.__on_change:
            self.__on_change(context)


class ProbedSet(set):
    """Definition of the class to make probed sets"""
    def __init__(self, items=None, probe=None,
                 on_change=None):
        """
        Init.

        [parameters]
        - items: default value of the collection

        - probe: callback called whenever the content of the collection
        is going to change.
        It should accept as argument an instance of probed.Context.
        It should return the same instance (edited or not) of probed.Context
        it got as argument, or return None to cancel the change operation.

        - on_change: callback called whenever the content of the collection changes.
        It should accept as argument an instance of probed.Context.

        """
        super().__init__(items if items else ())
        self.__probe = probe
        self.__on_change = on_change
        self.__changed = False

    @property
    def probe(self):
        return self.__probe

    @probe.setter
    def probe(self, val):
        self.__probe = val

    @property
    def on_change(self):
        return self.__on_change

    @on_change.setter
    def on_change(self, val):
        self.__on_change = val

    @property
    def changed(self):
        """
        Boolean attribute to indicate whether the content of the
        collection changed or not 
        """
        return self.__changed

    @changed.setter
    def changed(self, val):
        self.__changed = val

    def add(self, item):
        context = self.__get_context("add", item=item)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().add(context.item)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def clear(self):
        context = self.__get_context("clear")
        context = self.__run_probe(context)
        if not context:
            return
        val = super().clear()
        self.__changed = True
        self.__run_on_change(context)
        return val

    def difference_update(self, *others):
        context = self.__get_context("difference_update", others=others)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().difference_update(*context.others)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def discard(self, item):
        context = self.__get_context("discard", item=item)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().discard(context.item)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def intersection_update(self, *others):
        context = self.__get_context("intersection_update", others=others)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().intersection_update(*context.others)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def pop(self):
        context = self.__get_context("pop")
        context = self.__run_probe(context)
        if not context:
            return
        val = super().pop()
        self.__changed = True
        self.__run_on_change(context)
        return val

    def remove(self, item):
        context = self.__get_context("remove", item=item)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().remove(context.item)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def symmetric_difference_update(self, other):
        context = self.__get_context("symmetric_difference_update",
                               other=other)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().symmetric_difference_update(context.other)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def update(self, *others):
        context = self.__get_context("update", others=others)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().update(*context.others)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __iand__(self, *others):
        context = self.__get_context("iand", others=others)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__iand__(*context.others)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __ior__(self, *others):
        context = self.__get_context("ior", others=others)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__ior__(*context.others)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __isub__(self, *others):
        context = self.__get_context("isub", others=others)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__isub__(*context.others)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __ixor__(self, other):
        context = self.__get_context("ixor", other=other)
        context = self.__run_probe(context)
        if not context:
            return
        val = super().__ixor__(context.other)
        self.__changed = True
        self.__run_on_change(context)
        return val

    def __repr__(self):
        val = super().__repr__()
        a = "{}(".format(self.__class__.__name__)
        b = ")"
        if self and val.startswith(a) and val.endswith(b):
            val = val.lstrip(a).rstrip(b)
        return val

    def __get_context(self, operation, **kwargs):
        return Context(self, "set", operation, **kwargs)

    def __run_probe(self, context):
        if self.__probe:
            context = self.__probe(context)
        return context

    def __run_on_change(self, context):
        if self.__on_change:
            self.__on_change(context)


class Context:
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

    def on_change(context):
        context.container # 'dict'
        context.collection # the actual plist object
        context.operation # 'append'
        context.value # 'hello'

    plist = probed.ProbedList(on_change=on_change)
    plist.append("hello") # the name of the parameter of this operation is 'value'
    """
    def __init__(self, collection, container, operation,
                 **kwargs):
        """
        Init

        [parameters]
        - collection: the collection object
        - container: str, the type of container ("dict", "set", "list")
        - operation: str, the type of operation. Example: "pop", "remove", "append".
        """
        self._collection = collection
        self._container = container
        self._operation = operation
        if "item" in kwargs:
            self.item = kwargs["item"]
        if "key" in kwargs:
            self.key = kwargs["key"]
        if "index" in kwargs:
            self.index = kwargs["index"]
        if "value" in kwargs:
            self.value = kwargs["value"]
        if "default" in kwargs:
            self.default = kwargs["default"]
        if "other" in kwargs:
            self.other = kwargs["other"]
        if "others" in kwargs:
            self.others = kwargs["others"]
        if "reverse" in kwargs:
            self.reverse = kwargs["reverse"]

    @property
    def collection(self):
        return self._collection

    @property
    def container(self):
        return self._container

    @property
    def operation(self):
        return self._operation
