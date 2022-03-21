Back to [All Modules](https://github.com/pyrustic/probed/blob/master/docs/modules/README.md#readme)

# Module Overview

**probed**
 
No description

> **Classes:** &nbsp; [Context](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/Context.md#class-context) &nbsp;&nbsp; [ProbedDict](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedDict.md#class-probeddict) &nbsp;&nbsp; [ProbedList](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedList.md#class-probedlist) &nbsp;&nbsp; [ProbedSet](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedSet.md#class-probedset)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class ProbedSet
Definition of the class to make probed sets

## Base Classes
set

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
[\_probedset\_\_get\_context](#_ProbedSet__get_context) &nbsp;&nbsp; [\_probedset\_\_run\_on\_change](#_ProbedSet__run_on_change) &nbsp;&nbsp; [\_probedset\_\_run\_probe](#_ProbedSet__run_probe) &nbsp;&nbsp; [\_\_init\_\_](#__init__) &nbsp;&nbsp; [add](#add) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [difference\_update](#difference_update) &nbsp;&nbsp; [discard](#discard) &nbsp;&nbsp; [intersection\_update](#intersection_update) &nbsp;&nbsp; [pop](#pop) &nbsp;&nbsp; [remove](#remove) &nbsp;&nbsp; [symmetric\_difference\_update](#symmetric_difference_update) &nbsp;&nbsp; [update](#update)

## \_ProbedSet\_\_get\_context
None



**Signature:** (self, operation, \*\*kwargs)





**Return Value:** None.

[Back to Top](#module-overview)


## \_ProbedSet\_\_run\_on\_change
None



**Signature:** (self, context)





**Return Value:** None.

[Back to Top](#module-overview)


## \_ProbedSet\_\_run\_probe
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


## add
Add an element to a set.

This has no effect if the element is already present.



**Signature:** (self, item)





**Return Value:** None.

[Back to Top](#module-overview)


## clear
Remove all elements from this set.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## difference\_update
Remove all elements of another set from this set.



**Signature:** (self, \*others)





**Return Value:** None.

[Back to Top](#module-overview)


## discard
Remove an element from a set if it is a member.

If the element is not a member, do nothing.



**Signature:** (self, item)





**Return Value:** None.

[Back to Top](#module-overview)


## intersection\_update
Update a set with the intersection of itself and another.



**Signature:** (self, \*others)





**Return Value:** None.

[Back to Top](#module-overview)


## pop
Remove and return an arbitrary set element.
Raises KeyError if the set is empty.



**Signature:** (self)





**Return Value:** None.

[Back to Top](#module-overview)


## remove
Remove an element from a set; it must be a member.

If the element is not a member, raise a KeyError.



**Signature:** (self, item)





**Return Value:** None.

[Back to Top](#module-overview)


## symmetric\_difference\_update
Update a set with the symmetric difference of itself and another.



**Signature:** (self, other)





**Return Value:** None.

[Back to Top](#module-overview)


## update
Update a set with the union of itself and others.



**Signature:** (self, \*others)





**Return Value:** None.

[Back to Top](#module-overview)



