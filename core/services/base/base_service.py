from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, **kwargs):
        self.kwargs = self._normalize_recursive(kwargs)

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    def _normalize_recursive(self, value):
        if isinstance(value, dict):
            return {key: self._normalize_recursive(item) for key, item in value.items()}

        if isinstance(value, list):
            return [self._normalize_recursive(item) for item in value]

        if isinstance(value, str):
            return value.strip()

        return value