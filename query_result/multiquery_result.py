from query_result.base_query_result import BaseQueryResult
from query_result.iterators.multiquery_result_iterator import MultiQueryResultIterator
from query_result.query_result import QueryResult


class MultiQueryResult(BaseQueryResult):

    # ---------------------------------------------------------------
    # ITERACIÓN
    # ---------------------------------------------------------------
    def __iter__(self):
        """
        Returns an iterator for multiple query results.

        Returns:
            MultiQueryResultIterator: An iterator for multiple results.
        """
        return MultiQueryResultIterator(self._results, self._main_key)
    
    # ---------------------------------------------------------------
    # REPRESENTACION
    # ---------------------------------------------------------------
    def __repr__(self):
        """
        Returns a representation of the query result.

        Returns:
            str: String representation of the results.
        """
        queries = ""
        for query in self:
            queries += "\n"
            queries += repr(query)
        return f"MultiQueryResult({queries})"
    
    # ---------------------------------------------------------------
    # ACCESO
    # ---------------------------------------------------------------
    def _getitem_by_index(self, index):
        """
        Gets the result corresponding to a given index and returns it
        as an instance of `QueryResult`.

        Args:
            index (int): Index of the desired result.

        Returns:
            QueryResult: Result corresponding to the index.
        """
        result = super()._getitem_by_index(index)
        return QueryResult(result)
    
    def __getitem__(self, index):
        """
        Gets the result corresponding to the provided index or key.

        Args:
            index (int, str): Index or key of the desired result.

        Returns:
            QueryResult: Result corresponding to the provided index or key.

        Raises:
            TypeError: If the index is neither an integer nor a string.
        """
        return self._either_by_type(self._getitem_by_index, self._getitem_by_key, index)
    
    def _setitem_by_index(self, index, query):
        """
        Sets the given value corresponding to the provided index.

        Args:
            index (int, str): Index of the value to set.
            Query (QueryResult): Query to be set as the value.

        Raise:
            Error if the given index is greater than the number of queries.
        """
        for key in self._results.keys():
            old_value = self._results[key]
            if old_value is not None:
                old_value[index] = query[key]
            self._results[key] = old_value
    
    def _setitem_by_key(self, key, query):
        raise NotImplementedError("Not yet implemented. Use set by number.")

    def __setitem__(self, index, value):
        return self._either_by_type(self._setitem_by_index, self._setitem_by_key, index, value)