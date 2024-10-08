from inspect import isawaitable
from typing import AsyncIterable, Iterable, List, TypeVar, Union

T = TypeVar("T")


async def maybe_async_iterable_to_list(iterable: Union[Iterable[T], AsyncIterable[T]]) -> List[T]:
    items = []
    if isinstance(iterable, AsyncIterable):
        async for item in iterable:
            items.append(item)
    else:
        for item in iterable:
            items.append(item)
    return items


async def maybe_await(resp: T) -> T:
    if isawaitable(resp):
        resp = await resp
    return resp
