from abc import ABC, abstractmethod


class BaseOracleQuery(ABC):
    def __init__(self, **params):
        self.params = self._normalize_recursive(params)

    @abstractmethod
    def get_sql(self) -> str:
        raise NotImplementedError

    def get_params(self) -> dict:
        return {}

    def _normalize_recursive(self, value):
        if isinstance(value, dict):
            return {key: self._normalize_recursive(item) for key, item in value.items()}

        if isinstance(value, list):
            return [self._normalize_recursive(item) for item in value]

        if isinstance(value, str):
            return value.strip()

        return value