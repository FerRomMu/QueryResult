from query_result.iterators.basequery_result_iterator import BaseQueryResultIterator
from query_result.query_result import QueryResult


class MultiQueryResultIterator(BaseQueryResultIterator):
    """
    Iterator to handle multiple query results, formatting the
    results as instances of `QueryResult`.
    """

    def _format_result(self, query_result):
        """
        Formats the query result as an instance of `QueryResult`.

        Args:
            query_result (dict): Query result in dictionary format.

        Returns:
            QueryResult: Formatted result.
        """
        return QueryResult(query_result)