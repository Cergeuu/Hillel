from abc import ABC, abstractmethod


#### Створити клас з абстрактним методом. Створити об'єкт даного класу.
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


# Створення об'єкту класу AbstractClass
obj = AbstractClass()


### Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.


class BaseClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


class DerivedClass(BaseClass):
    def abstract_method(self):
        print("Implementation of abstract_method in DerivedClass")


# Створення об'єкту класу DerivedClass
obj2 = DerivedClass()
obj2.abstract_method()


### Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.


class AbstractBaseClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


class NewClass(AbstractBaseClass):
    def abstract_method(self):
        print("Implementation of abstract_method in NewClass")


# Створення об'єкту класу NewClass
obj3 = NewClass()
obj3.abstract_method()
