from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any, Callable, Union, Set, Optional
import asyncio
import inspect
from dataclasses import dataclass

# --- Strategy ---

DataInput = TypeVar("DataInput")
DataOutput = TypeVar("DataOutput")

StrategyCallback = Callable[[DataInput], DataOutput]

class Strategy(ABC, Generic[DataInput, DataOutput]):
    @abstractmethod
    def execute(self, data_input:DataInput) -> DataOutput:
        pass

class AsyncStrategy(ABC, Generic[DataInput, DataOutput]):
    @abstractmethod
    async def execute(self, data_input:DataInput) -> DataOutput:
        pass

# --- Observer ---

T = TypeVar("T")

class Observer(ABC, Generic[T]):
    @abstractmethod
    def update(self, data: T) -> None:
        pass

ObserverCallback = Union[Observer[T], Callable[[T], None]]

class Subject(ABC, Generic[T]):

    def __init__(self) -> None:
        self._observers: Set[ObserverCallback[T]] = set()

    def attach(self, observer: ObserverCallback[T]) -> None:
        self._observers.add(observer)

    def detach(self, observer: ObserverCallback[T]) -> None:
        self._observers.discard(observer)

    def notify(self, data: T) -> None:
        for observer in list(self._observers):
            if isinstance(observer, Observer):
                observer.update(data)
            elif callable(observer):
                observer(data)

class AsyncSubject(Subject[T]):
    async def notify_async(self, data: T) -> None:
        """Notifica observadores de forma assíncrona."""
        tasks = []
        for observer in list(self._observers):
            if isinstance(observer, Observer):
                # Se o update da classe for assíncrono ou síncrono
                if inspect.iscoroutinefunction(observer.update):
                    tasks.append(observer.update(data))
                else:
                    observer.update(data)
            elif callable(observer):
                if inspect.iscoroutinefunction(observer):
                    tasks.append(observer(data))
                else:
                    observer(data)

        if tasks:
            await asyncio.gather(*tasks)

# --- Chain of Responsibility ---

RequestT = TypeVar("RequestT")  # O tipo do dado/requisição que trafega na corrente
ResponseT = TypeVar("ResponseT")  # O tipo do retorno (se houver)


class Handler(ABC, Generic[RequestT, ResponseT]):
    """
    Classe base abstrata para a Corrente de Responsabilidade.
    """

    def __init__(self) -> None:
        self._next_handler: Optional[Handler[RequestT, ResponseT]] = None

    def set_next(self, handler: Handler[RequestT, ResponseT]) -> Handler[RequestT, ResponseT]:
        """
        Define o próximo manipulador na corrente e o retorna.
        Isso permite encadeamento fluido: h1.set_next(h2).set_next(h3)
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: RequestT) -> Optional[ResponseT]:
        """
        Processa a requisição ou a repassa para o próximo da corrente.
        """
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class AsyncHandler(ABC, Generic[RequestT, ResponseT]):
    def __init__(self) -> None:
            self._next_handler: Optional[Handler[RequestT, ResponseT]] = None
    
    def set_next(self, handler: Handler[RequestT, ResponseT]) -> Handler[RequestT, ResponseT]:
        """
        Define o próximo manipulador na corrente e o retorna.
        Isso permite encadeamento fluido: h1.set_next(h2).set_next(h3)
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    async def handle(self, request: RequestT) -> Optional[ResponseT]:

        if self._next_handler:
            return await self._next_handler.handle(request)