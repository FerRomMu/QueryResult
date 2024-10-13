from query_result.iterators.basequery_result_iterator import BaseQueryResultIterator
from query_result.query_result import QueryResult


class MultiQueryResultIterator(BaseQueryResultIterator):
    """
    Iterador para manejar múltiples resultados de consulta, formateando los
    resultados como instancias de `QueryResult`.
    """

    def _format_result(self, query_result):
        """
        Formatea el resultado de la consulta como una instancia de `QueryResult`.

        Args:
            query_result (dict): Resultado de la consulta en formato de diccionario.

        Returns:
            QueryResult: Resultado formateado.
        """
        return QueryResult(query_result)