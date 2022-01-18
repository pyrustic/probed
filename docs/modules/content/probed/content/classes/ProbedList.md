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

# Class ProbedList
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.

## Base Classes
list

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
[\_probedlist\_\_get\_info](#_ProbedList__get_info) &nbsp; [\_probedlist\_\_run\_on\_change](#_ProbedList__run_on_change) &nbsp; [\_probedlist\_\_run\_probe](#_ProbedList__run_probe) &nbsp; [\_\_init\_\_](#__init__) &nbsp; [append](#append) &nbsp; [clear](#clear) &nbsp; [copy](#copy) &nbsp; [count](#count) &nbsp; [extend](#extend) &nbsp; [index](#index) &nbsp; [insert](#insert) &nbsp; [pop](#pop) &nbsp; [remove](#remove) &nbsp; [reverse](#reverse) &nbsp; [sort](#sort)

## \_ProbedList\_\_get\_info
No description



**Signature:** (self, operation, \*\*kwargs)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedList\_\_run\_on\_change
No description



**Signature:** (self, info)



**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedList\_\_run\_probe
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


## append
Append object to the end of the list.



**Signature:** (self, value)



**Return Value:** None

[Back to Top](#module-overview)


## clear
Remove all items from list.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## copy
Return a shallow copy of the list.

**Inherited from:** list

**Signature:** (self, /)



**Return Value:** None

[Back to Top](#module-overview)


## count
Return number of occurrences of value.

**Inherited from:** list

**Signature:** (self, value, /)



**Return Value:** None

[Back to Top](#module-overview)


## extend
Extend list by appending elements from the iterable.



**Signature:** (self, value)



**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** list

**Signature:** (self, value, start=0, stop=9223372036854775807, /)



**Return Value:** None

[Back to Top](#module-overview)


## insert
Insert object before index.



**Signature:** (self, index, value)



**Return Value:** None

[Back to Top](#module-overview)


## pop
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.



**Signature:** (self, index=-1)



**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove first occurrence of value.

Raises ValueError if the value is not present.



**Signature:** (self, value)



**Return Value:** None

[Back to Top](#module-overview)


## reverse
Reverse *IN PLACE*.



**Signature:** (self)



**Return Value:** None

[Back to Top](#module-overview)


## sort
Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them,
ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.



**Signature:** (self, \*, key=None, reverse=False)



**Return Value:** None

[Back to Top](#module-overview)



