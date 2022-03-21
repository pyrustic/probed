Back to [All Modules](https://github.com/pyrustic/probed/blob/master/docs/modules/README.md#readme)

# Module Overview

**probed**
 
No description

> **Classes:** &nbsp; [Context](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/Context.md#class-context) &nbsp;&nbsp; [ProbedDict](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedDict.md#class-probeddict) &nbsp;&nbsp; [ProbedList](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedList.md#class-probedlist) &nbsp;&nbsp; [ProbedSet](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedSet.md#class-probedset)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class ProbedDict
Definition of the class to make probed dicts

## Base Classes
dict

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|changed|getter|Boolean attribute to indicate whether the content of the collection changed or not ||
|changed|setter|None||
|on_change|getter|None||
|on_change|setter|None||
|probe|getter|None||
|probe|setter|None||



# All Methods
[\_probeddict\_\_get\_context](#_ProbedDict__get_context) &nbsp;&nbsp; [\_probeddict\_\_merge\_update\_other\_kwargs](#_ProbedDict__merge_update_other_kwargs) &nbsp;&nbsp; [\_probeddict\_\_run\_on\_change](#_ProbedDict__run_on_change) &nbsp;&nbsp; [\_probeddict\_\_run\_probe](#_ProbedDict__run_probe) &nbsp;&nbsp; [\_\_init\_\_](#__init__) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [fromkeys](#fromkeys) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [pop](#pop) &nbsp;&nbsp; [popitem](#popitem) &nbsp;&nbsp; [setdefault](#setdefault) &nbsp;&nbsp; [update](#update)

## \_ProbedDict\_\_get\_context
None



**Signature:** (self, operation, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)


## \_ProbedDict\_\_merge\_update\_other\_kwargs
None



**Signature:** (self, other, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)


## \_ProbedDict\_\_run\_on\_change
None



**Signature:** (self, context)





**Return Value:** None.

[Back to Top](#module-overview)


## \_ProbedDict\_\_run\_probe
None



**Signature:** (self, context)





**Return Value:** None.

[Back to Top](#module-overview)


## \_\_init\_\_
Init.




**Signature:** (self, items=None, probe=None, on\_change=None)

|Parameter|Description|
|---|---|
|items|default value of the collection |
|probe|callback called whenever the content of the collection is going to change. It should accept as argument an instance of probed.Context. It should return the same instance (edited or not) of probed.Context it got as argument, or return None to cancel the change operation. |
|on\_change|callback called whenever the content of the collection changes. It should accept as argument an instance of probed.Context.|





**Return Value:** None.

[Back to Top](#module-overview)


## clear
D.clear() -> None.  Remove all items from D.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## fromkeys
Create a new dictionary with keys from iterable and values set to value.

**Inherited from:** dict

**Signature:** (type, iterable, value=None, /)





**Return Value:** None.

[Back to Top](#module-overview)


## get
Return the value for key if key is in the dictionary, else default.

**Inherited from:** dict

**Signature:** (self, key, default=None, /)





**Return Value:** None.

[Back to Top](#module-overview)


## pop
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised



**Signature:** (self, key, default=None)





**Return Value:** None.

[Back to Top](#module-overview)


## popitem
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## setdefault
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.



**Signature:** (self, key, default=None)





**Return Value:** None.

[Back to Top](#module-overview)


## update
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]



**Signature:** (self, other=None, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)



