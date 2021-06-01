class ProbedDict(dict):

    def __init__(self, items=None, probe=None,
                 on_change=None):
        super().__init__(items if items else {})
        self.__probe = probe
        self.__on_change = on_change
        self.__changed = False

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, val):
        self.__changed = val

    def clear(self):
        info = self.__get_info("clear")
        info = self.__run_probe(info)
        if not info:
            return
        val = super().clear()
        self.__changed = True
        self.__run_on_change(info)
        return val

    def pop(self, key, default=None):
        info = self.__get_info("pop", key=key,
                               default=default)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().pop(info.key, info.default)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def popitem(self):
        info = self.__get_info("popitem")
        info = self.__run_probe(info)
        if not info:
            return
        val = super().popitem()
        self.__changed = True
        self.__run_on_change(info)
        return val

    def setdefault(self, key, default=None):
        info = self.__get_info("setdefault", key=key,
                               default=default)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().setdefault(info.key, info.default)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def update(self, other=None, **kwargs):
        other = self.__merge_update_other_kwargs(other,
                                                 **kwargs)
        info = self.__get_info("update", other=other)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().update(other)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __delitem__(self, key):
        info = self.__get_info("delitem", key=key)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__delitem__(info.key)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __setitem__(self, key, value):
        info = self.__get_info("setitem", key=key,
                               value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__setitem__(info.key, info.value)
        self.__changed = True
        self.__run_on_change(info)
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

    def __get_info(self, operation, **kwargs):
        return Info(self, "dict", operation, **kwargs)

    def __run_probe(self, info):
        if self.__probe:
            info = self.__probe(info)
        return info

    def __run_on_change(self, info):
        if self.__on_change:
            self.__on_change(info)


class ProbedList(list):

    def __init__(self, items=None, probe=None,
                 on_change=None):
        super().__init__(items if items else ())
        self.__probe = probe
        self.__on_change = on_change
        self.__changed = False

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, val):
        self.__changed = val

    def append(self, value):
        info = self.__get_info("append", value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().append(info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def clear(self):
        info = self.__get_info("clear")
        info = self.__run_probe(info)
        if not info:
            return
        val = super().clear()
        self.__changed = True
        self.__run_on_change(info)
        return val

    def extend(self, value):
        info = self.__get_info("extend", value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().extend(info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def insert(self, index, value):
        info = self.__get_info("insert", index=index,
                               value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().insert(info.index, info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def pop(self, index=-1):
        info = self.__get_info("pop", index=index)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().pop(info.index)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def remove(self, value):
        info = self.__get_info("remove", value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().remove(info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def reverse(self):
        info = self.__get_info("reverse")
        info = self.__run_probe(info)
        if not info:
            return
        val = super().reverse()
        self.__changed = True
        self.__run_on_change(info)
        return val

    def sort(self, *, key=None, reverse=False):
        info = self.__get_info("sort", key=key,
                               reverse=reverse)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().sort(key=info.key, reverse=info.reverse)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __delitem__(self, index):
        info = self.__get_info("delitem", index=index)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__delitem__(info.index)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __iadd__(self, value):
        info = self.__get_info("iadd", value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__iadd__(info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __imul__(self, value):
        info = self.__get_info("imul", value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__imul__(info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __setitem__(self, index, value):
        info = self.__get_info("setitem", index=index,
                               value=value)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__setitem__(info.index, info.value)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __get_info(self, operation, **kwargs):
        return Info(self, "list", operation, **kwargs)

    def __run_probe(self, info):
        if self.__probe:
            info = self.__probe(info)
        return info

    def __run_on_change(self, info):
        if self.__on_change:
            self.__on_change(info)


class ProbedSet(set):

    def __init__(self, items=None, probe=None,
                 on_change=None):
        super().__init__(items if items else ())
        self.__probe = probe
        self.__on_change = on_change
        self.__changed = False

    @property
    def changed(self):
        return self.__changed

    @changed.setter
    def changed(self, val):
        self.__changed = val

    def add(self, item):
        info = self.__get_info("add", item=item)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().add(info.item)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def clear(self):
        info = self.__get_info("clear")
        info = self.__run_probe(info)
        if not info:
            return
        val = super().clear()
        self.__changed = True
        self.__run_on_change(info)
        return val

    def difference_update(self, *others):
        info = self.__get_info("difference_update", others=others)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().difference_update(*info.others)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def discard(self, item):
        info = self.__get_info("discard", item=item)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().discard(info.item)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def intersection_update(self, *others):
        info = self.__get_info("intersection_update", others=others)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().intersection_update(*info.others)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def pop(self):
        info = self.__get_info("pop")
        info = self.__run_probe(info)
        if not info:
            return
        val = super().pop()
        self.__changed = True
        self.__run_on_change(info)
        return val

    def remove(self, item):
        info = self.__get_info("remove", item=item)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().remove(info.item)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def symmetric_difference_update(self, other):
        info = self.__get_info("symmetric_difference_update",
                               other=other)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().symmetric_difference_update(info.other)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def update(self, *others):
        info = self.__get_info("update", others=others)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().update(*info.others)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __iand__(self, *others):
        info = self.__get_info("iand", others=others)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__iand__(*info.others)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __ior__(self, *others):
        info = self.__get_info("ior", others=others)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__ior__(*info.others)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __isub__(self, *others):
        info = self.__get_info("isub", others=others)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__isub__(*info.others)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __ixor__(self, other):
        info = self.__get_info("ixor", other=other)
        info = self.__run_probe(info)
        if not info:
            return
        val = super().__ixor__(info.other)
        self.__changed = True
        self.__run_on_change(info)
        return val

    def __repr__(self):
        val = super().__repr__()
        a = "{}(".format(self.__class__.__name__)
        b = ")"
        if self and val.startswith(a) and val.endswith(b):
            val = val.lstrip(a).rstrip(b)
        return val

    def __get_info(self, operation, **kwargs):
        return Info(self, "set", operation, **kwargs)

    def __run_probe(self, info):
        if self.__probe:
            info = self.__probe(info)
        return info

    def __run_on_change(self, info):
        if self.__on_change:
            self.__on_change(info)


class Info:
    def __init__(self, collection, container, operation,
                 **kwargs):
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
