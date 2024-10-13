from query_result.base_query_result import BaseQueryResult
from query_result.iterators.query_result_iterator import QueryResultIterator


class QueryResult(BaseQueryResult):
    """
    Result of an individual query.
    """
    # ---------------------------------------------------------------
    # ITERACIÓN
    # ---------------------------------------------------------------
    def __iter__(self):
        """
        Returns an iterator for the query results.

        Returns:
            QueryResultIterator: An iterator for the query results.
        """
        return QueryResultIterator(self._results, self._main_key)

    def drop_all(self, indexes):
        """
        Removes the values of the given indices.

        Args:
            indexes (list[int]): A list of indices of results to delete.
        """
        for key in self._results.keys():
            old_values = self._results[key]
            if old_values is not None:
                new_values = [v for i, v in enumerate(old_values) if i not in indexes]
                self._results[key] = new_values
