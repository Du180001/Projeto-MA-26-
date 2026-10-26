from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any
# Para Python 3.11+:
from typing import Self 

# --- SINGLETON ---

class SingletonMeta(type):
    """
    Metaclasse para criação de Singletons thread-safe.
    Cada classe que usar esta metaclasse terá apenas UMA instância única.
    """
    _instances: dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# --- FACTORY ---

T = TypeVar("T")

class Factory(ABC, Generic[T]):
    """
    Classe base abstrata para criação de Factories.
    """

    @abstractmethod
    def factory_method(self) -> T:
        """Cria e retorna um novo objeto produto."""
        pass


# --- BUILDER ---

class Builder(ABC, Generic[T]):
    """
    Classe base abstrata para criação de Builders.
    """

    @abstractmethod
    def reset(self) -> Self:
        """Reinicia o estado do builder e retorna a si mesmo."""
        pass

    @abstractmethod
    def build(self) -> T:
        """Constrói e retorna o objeto final."""
        pass