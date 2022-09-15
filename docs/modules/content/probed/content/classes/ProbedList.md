Back to [All Modules](https://github.com/pyrustic/probed/blob/master/docs/modules/README.md#readme)

# Module Overview

**probed**
 
No description

> **Classes:** &nbsp; [Context](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/Context.md#class-context) &nbsp;&nbsp; [ProbedDict](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedDict.md#class-probeddict) &nbsp;&nbsp; [ProbedList](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedList.md#class-probedlist) &nbsp;&nbsp; [ProbedSet](https://github.com/pyrustic/probed/blob/master/docs/modules/content/probed/content/classes/ProbedSet.md#class-probedset)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class ProbedList
Definition of the class to make probed lists

## Base Classes
list

## Class Attributes
No class attributes.

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
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [append](#append) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [copy](#copy) &nbsp;&nbsp; [count](#count) &nbsp;&nbsp; [extend](#extend) &nbsp;&nbsp; [index](#index) &nbsp;&nbsp; [insert](#insert) &nbsp;&nbsp; [pop](#pop) &nbsp;&nbsp; [remove](#remove) &nbsp;&nbsp; [reverse](#reverse) &nbsp;&nbsp; [sort](#sort) &nbsp;&nbsp; [\_probedlist\_\_get\_context](#_ProbedList__get_context) &nbsp;&nbsp; [\_probedlist\_\_run\_on\_change](#_ProbedList__run_on_change) &nbsp;&nbsp; [\_probedlist\_\_run\_probe](#_ProbedList__run_probe)

## \_\_init\_\_
Init.




**Signature:** (self, items=None, probe=None, on\_change=None)

|Parameter|Description|
|---|---|
|items|default value of the collection |
|probe|callback called whenever the content of the collection is going to change. It should accept as argument an instance of probed.Context. It should return the same instance (edited or not) of probed.Context it got as argument, or return None to cancel the change operation. |
|on\_change|callback called whenever the content of the collection changes. It should accept as argument an instance of probed.Context.|





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


## \_ProbedList\_\_get\_context
No description



**Signature:** (self, operation, \*\*kwargs)





**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedList\_\_run\_on\_change
No description



**Signature:** (self, context)





**Return Value:** None

[Back to Top](#module-overview)


## \_ProbedList\_\_run\_probe
No description



**Signature:** (self, context)





**Return Value:** None

[Back to Top](#module-overview)



