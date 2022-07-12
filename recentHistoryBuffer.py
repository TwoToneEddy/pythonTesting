from typing import Generic, Optional, overload, TypeVar, Union
import numpy as np

ValType = TypeVar("ValType")


class RecentHistoryBuffer(Generic[ValType]):
    def __init__(
        self,
        length: int,
        *,
        dtype=np.float64,
        fill: Optional[ValType] = None,
    ) -> None:
        self._l = length
        self._last_written_index = 0
        self._data: np.ndarray = np.empty(shape=(length,), dtype=dtype)
        self.fill(fill)

    def min(self) -> ValType:
        # Get the lowest value in the buffer.
        # Useful for minimum recently seen problems.
        return np.min(self._data)

    def max(self) -> ValType:
        # Get the lowest value in the buffer.
        # Useful for maximum recently seen problems.
        return np.max(self._data)

    def getArr(self) -> np.ndarray:
        return self._data

    def fill(self, fill: Optional[ValType] = None) -> None:
        """
        Fill the buffer with the provided value for initialisation
        """
        if fill is None:
            self._data[:] = np.nan
        else:
            self._data[:] = fill

    def __len__(self) -> int:
        self._l

    def __setitem__(self, key: int, value: ValType) -> None:
        self._last_written_index = max(key, self._last_written_index)
        self._data[key % self._l] = value

    @overload
    def __getitem__(self, key: int) -> ValType:
        ...

    @overload
    def __getitem__(self, key: slice) -> np.ndarray:
        ...

    def __getitem__(self, key: Union[int, slice]) -> Union[ValType, np.ndarray]:
        if isinstance(key, int):
            assert (
                key <= self._last_written_index
            ), "Reading past the last written value"
            return self._data[key % self._l]  # type: ignore
        elif isinstance(key, slice):
            assert (
                key.stop <= self._last_written_index
            ), "Reading slice past last written value"
            assert key.stop > key.start, "RingBuffer slice stops before it starts"
            assert (
                key.stop - key.start <= self._l
            ), "RingBuffer slice is longer than buffer length"
            s = slice(
                key.start % self._l,
                key.stop % self._l,
                key.step,
            )
            return self._data[s]

