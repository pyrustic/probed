Back to [All Modules](https://github.com/pyrustic/probed/blob/master/docs/modules/README.md#readme)

# Module Overview

> **probed**
> 
> No description
>
> **Classes:** &nbsp; [Info](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/Info.md#class-info) &nbsp; [ProbedDict](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedDict.md#class-probeddict) &nbsp; [ProbedList](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedList.md#class-probedlist) &nbsp; [ProbedSet](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedSet.md#class-probedset)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class ProbedSet
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.

## Base Classes
set

## Class Attributes


## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|changed|getter|Boolean attribute to indicate whether the content of the
collection changed or not ||
|changed|setter|None||
|on_change|getter|None||
|on_change|setter|None||
|probe|getter|None||
|probe|setter|None||



# All Methods
[\_probedset\_\_get\_info](#_ProbedSet__get_info) &nbsp; [\_probedset\_\_run\_on\_change](#_ProbedSet__run_on_change) &nbsp; [\_probedset\_\_run\_probe](#_ProbedSet__run_probe) &nbsp; [\_\_init\_\_](#__init__) &nbsp; [add](#add) &nbsp; [clear](#clear) &nbsp; [difference\_update](#difference_update) &nbsp; [discard](#discard) &nbsp; [intersection\_update](#intersection_update) &nbsp; [pop](#pop) &nbsp; [remove](#remove) &nbsp; [symmetric\_difference\_update](#symmetric_difference_update) &nbsp; [update](#update)

## \_ProbedSet\_\_get\_info
No description



**Signature:** (self, operation, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedSet\_\_run\_on\_change
No description



**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedSet\_\_run\_probe
No description



**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_\_init\_\_
- items: default value of the collection

- probe: callback called whenever the content of the collection
is going to change.
It should accept as argument an instance of probed.Info.
It should return the same instance (edited or not) of probed.Info
it got as argument, or return None to cancel the change operation.

- on_change: callback called whenever the content of the collection changes.
It should accept as argument an instance of probed.Info.



**Signature:** (self, items=None, probe=None, on\_change=None)



**Return Value:** None

[Back to Top](#module-overview)


## add
Add an element to a set.

This has no effect if the element is already present.



**Signature:** (self, item)



**Return Value:** None

[Back to Top](#module-overview)


## clear
Remove all elements from this set.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## difference\_update
Remove all elements of another set from this set.



**Signature:** (self, \*others)



**Return Value:** None

[Back to Top](#module-overview)


## discard
Remove an element from a set if it is a member.

If the element is not a member, do nothing.



**Signature:** (self, item)



**Return Value:** None

[Back to Top](#module-overview)


## intersection\_update
Update a set with the intersection of itself and another.



**Signature:** (self, \*others)



**Return Value:** None

[Back to Top](#module-overview)


## pop
Remove and return an arbitrary set element.
Raises KeyError if the set is empty.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove an element from a set; it must be a member.

If the element is not a member, raise a KeyError.



**Signature:** (self, item)



**Return Value:** None

[Back to Top](#module-overview)


## symmetric\_difference\_update
Update a set with the symmetric difference of itself and another.



**Signature:** (self, other)



**Return Value:** None

[Back to Top](#module-overview)


## update
Update a set with the union of itself and others.



**Signature:** (self, \*others)



**Return Value:** None

[Back to Top](#module-overview)



