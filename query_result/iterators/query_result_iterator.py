from query_result.iterators.basequery_result_iterator import BaseQueryResultIterator


class QueryResultIterator(BaseQueryResultIterator):
    """
    Iterator to handle a single query result, returning the
    results in the original format without modifications.
    """

    def _format_result(self, query_result):
        """
        Returns the query result as is.

        Args:
            query_result (dict): Query result in dictionary format.

        Returns:
            dict: Unformatted query result.
        """
        return query_result