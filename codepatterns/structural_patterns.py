from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any
import asyncio
from functools import wraps

T = TypeVar("T")
A = TypeVar("A")

# --- Adapter ---

class Adapter(ABC, Generic[A, T]):
    """
    Classe base abstrata para criação de Adapters.
    Adapta um objeto do tipo 'A' (Adaptee) para a interface do tipo 'T' (Target).
    """

    def __init__(self, adaptee: A) -> None:
        self._adaptee: A = adaptee

    @property
    def adaptee(self) -> A:
        return self._adaptee

    @abstractmethod
    def adapt(self) -> T:
        pass

# --- Facade ---

class Facade (ABC):
    """
    Classe base abstrata para criação de Facades.
    Simplifica processos coordenados em uma instância.
    """

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class AsyncFacade(ABC):
    """
    Classe base abstrata para Facades Assíncronas (asyncio).
    Simplifica processos cordenados de forma assíncrona.
    """

    @abstractmethod
    async def execute(self) -> None:
        pass

    @abstractmethod
    async def stop(self) -> None:
        pass