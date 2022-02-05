# Copyright © Alaa-Sy-Dam-Sw. 2022

# The only granted permission, to any person obtaining a copy of these
# software, documentation, and source code files 
# is READING THE FILES ONLY FOR EDUCATIONAL PURPOSES, 
# subject to the following conditions:

# THIS SOFTWARE, DOCUMENTANTION AND SOURCE CODE FILES ARE
# PROVIDED, AS-IS, WITHOUT ANY EXPRESS or IMPLIED WARRANTY.

# IN NO EVENT WILL THE AUTHOR (COPYRIGHT HOLDER) BE HELD LIABLE FOR
# ANY KIND OF DAMAGE, CLAIM, OR ANY OTHER LIABILITY,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE, DOCUMENTANTION AND SOURCE CODE FILES. 

# IN NO EVENT WILL THE AUTHOR (COPYRIGHT HOLDER) BE HELD LIABLE FOR
# ANY KIND OF DAMAGE, CLAIM, OR ANY OTHER LIABILITY,
# ARISING FROM, OUT OF OR IN CONNECTION WITH 
# THE USE OR OTHER DEALINGS IN THE
# SOFTWARE, DOCUMENTANTION, AND SOURCE CODE FILES.
# RECALLING THAT THE ONLY PERMITED USE IS 
# "READING THE FILES ONLY FOR EDUCATIONAL PURPOSES".

"""An updated version of the native abc (abstract base class) module.

The module adds a new decorator to the native abc module.
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


The module still provides the same interface of the native abc module, 
and it didn't edit its internal implementation.

Example:
    Here is a typical usage example:
    
        from abc_updated import abstractattribute      
        from abc_updated import abstractproperty
        from abc_updated import ABC
        
        class AbstractPoint(ABC):        
           
            @abstractattribute
            def x(self):
                pass
          
            @abstractattribute
            def y(self):
                pass
            
            @abstractproperty
            def distance_from_origin(self):
                pass
    
        
        
        class PointFirstImplementation(AbstractPoint):            
           
            def __init__(self, x, y):
                self.x=x
                self.y=y
            
            @property
            def distance_from_origin(self):
                return (self.x**2 + self.y**2)**0.5

        class PointSecondImplementation(AbstractPoint):            
           
            def __init__(self, x, y):
                self._x=x
                self._y=y
    
            @property
            def x(self):
                return self._x       
    
            @x.setter
            def x(self, x):
                self._x=x
    
            @property
            def y(self):
                return self._y
    
            @y.setter
            def y(self, y):
                self._y=x
    
    
            @property
            def distance_from_origin(self):
                return (self.x**2 + self.y**2)**0.5
        
       
        point=PointFirstImplementation(1,2)
        print(point.x)
        print(point.y)
        print(point.distance_from_origin)
        point=PointSecondImplementation(1,2)
        print(point.x)
        print(point.y)
        print(point.distance_from_origin)

Exportables:
    A brief description of the exported classes, functions and
    module variables:
        ABC (class): an updated version of abc.ABC class
            enables the @abstractattribute decorator.
        ABCMeta (class): an updated version of abc.ABCMeta class
            enables the @abstractattribute decorator.
        abstractattribute (function): a new A decorator 
            indicating abstract attributes.
        abstractclassmethod (class): the same abc.abstractclassmethod class.
        abstractmethod (function): the same abc.abstractmethod function.
        abstractproperty (class): the same abc.abstractproperty class.
        abstractstaticmethod (class): the same abc.abstractstaticmethod class.

Todo:
    *Done
"""

import abc

abstractproperty = abc.abstractproperty 
abstractclassmethod = abc.abstractclassmethod
abstractstaticmethod = abc.abstractstaticmethod
abstractmethod = abc.abstractmethod


def abstractattribute(attribute: object = None) -> object:
    """A decorator indicating abstract attributes.
    
    This decorator enables us to define an abstract attribute.
    
    Args:
        attribute: the attribute that will be decorated as abstractattribute.
    
    Returns:
        the decorated attribute: attribute.__is_abstract_attribute__ = True.
    """
    if attribute is None:
        # create a dummy attribute object
        attribute = type("DummyAttribute",(),{})()
    attribute.__is_abstract_attribute__ = True
    return attribute


class ABCMeta(abc.ABCMeta):
    """ Metaclass for defining Abstract Base Classes (ABCs).
    
    This class inherits from the native abc.ABCMeta,
    and overrides the __Call__ method to enable
    the @abstractattribute decorator.
    
    Attributes:
        ---------
    """
    
    def __call__(cls, *args, **kwargs):
        instance = abc.ABCMeta.__call__(cls, *args, **kwargs)
        abstract_attributes = {
            name
            for name in dir(instance)
            if getattr(
                   getattr(instance, name),
                   '__is_abstract_attribute__',
                   False,
               )
        }
        if abstract_attributes:
            raise NotImplementedError(
                "Can't instantiate abstract class {} with"
                " abstract attributes: {}".format(
                    cls.__name__,
                    ', '.join(abstract_attributes)
                )
            )
        return instance


class ABC(metaclass=ABCMeta):
    """ABC is an updated version of the native abc.ABC helper class.
    
    The goal of the update is to enable the @abstractattribute decorator.
    
    Attributes:
        ---------
    """