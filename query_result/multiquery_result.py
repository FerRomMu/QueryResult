from query_result.base_query_result import BaseQueryResult
from query_result.iterators.multiquery_result_iterator import MultiQueryResultIterator
from query_result.query_result import QueryResult


class MultiQueryResult(BaseQueryResult):

    # ---------------------------------------------------------------
    # ITERACIÓN
    # ---------------------------------------------------------------
    def __iter__(self):
        """
        Devuelve un iterador para los múltiples resultados de consulta.

        Returns:
            MultiQueryResultIterator: Un iterador para los resultados múltiples.
        """
        return MultiQueryResultIterator(self._results, self._main_key)
    
    # ---------------------------------------------------------------
    # REPRESENTACION
    # ---------------------------------------------------------------
    def __repr__(self):
        """
        Devuelve una representación del query result.

        Returns:
        str: Representación en cadena de los resultados.
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
        Obtiene el resultado correspondiente a un índice dado y lo devuelve
        como una instancia de `QueryResult`.

        Args:
            index (int): Índice del resultado deseado.

        Returns:
            QueryResult: Resultado correspondiente al índice.
        """
        result = super()._getitem_by_index(index)
        return QueryResult(result)
    
    def __getitem__(self, index):
        """
        Obtiene el resultado correspondiente al índice o clave proporcionada.

        Args:
            index (int, str): Índice o clave del resultado deseado.

        Returns:
            QueryResult: Resultado correspondiente al índice o clave proporcionada.

        Raises:
            TypeError: Si el índice no es ni entero ni cadena.
        """
        return self._either_by_type(self._getitem_by_index, self._getitem_by_key, index)
    
    def _setitem_by_index(self, index, query):
        """
        Settea el valor dado correspondiente al índice proporcionado.

        Args:
            index (int, str): Índice del valor a settear.
            Query (QueryResult): Query a poner como valor.

        Raise:
            Error si el indice dado es mas grande que la cantidad de queries.
        """
        for key in self._results.keys():
            old_value = self._results[key]
            if old_value is not None:
                old_value[index] = query[key]
            self._results[key] = old_value
    
    def _setitem_by_key(self, key, query):
        raise NotImplementedError("Aún no implementado. Usar setteo númerico.")

    def __setitem__(self, index, value):
        return self._either_by_type(self._setitem_by_index, self._setitem_by_key, index, value)