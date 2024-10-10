from query_result.base_query_result import BaseQueryResult
from query_result.iterators.query_result_iterator import QueryResultIterator


class QueryResult(BaseQueryResult):
    """ 
    Resultado de una consulta individual.
    """
    # ---------------------------------------------------------------
    # ITERACIÓN
    # ---------------------------------------------------------------
    def __iter__(self):
        """
        Devuelve un iterador para los resultados de la consulta.

        Returns:
            QueryResultIterator: Un iterador para los resultados de la consulta.
        """
        return QueryResultIterator(self._results, self._main_key)

    def drop_all(self, indexes):
        """
        Elimina los valores de los indices dados.

        Args:
            indexes (list[int]): Una lista de indeces de resultados a borrar.
        """
        for key in self._results.keys():
            old_values = self._results[key]
            if old_values is not None:
                new_values = [v for i, v in enumerate(old_values) if i not in indexes]
                self._results[key] = new_values
