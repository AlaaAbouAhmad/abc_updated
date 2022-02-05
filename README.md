# abc_updated

An updated version of the native python abc (abstract base class) module.

This module adds a new decorator to the native abc module.
The new decorator is called "@abstractattribute", and it converts
its input into an abstract attribute that can be implemented
and initialized as an attribute inside the derived classes' __init__ method,
or even can be implemented as a propety inside that derived class.

We recommend to use this new decorator to replace the native @abstractproperty
decorator in the cases that require implementing both the setter 
and the getter methods in the derived classes.
Because  in such cases we are violating the abstraction concept,
as we are enforcing the developer who needs to implement our abstraction
to implement both the setter and the getter methods,
althoug the actual implemetation of these methods might not require
any computation, so the property is unnecessary, and it is better,
in such cases, to implement the abstract property by defining
a public attribute (inside the __init__ method).
The new decorator @abstractattribute, actually enables us to do that.


The module provides the same interface of the native abc module, 
and it didn't edit its internal implementation.

The code is compatible with <a href="https://google.github.io/styleguide/pyguide.html"> <b>Google Python Style Guide </b> </a>
