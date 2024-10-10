from query_result.iterators.basequery_result_iterator import BaseQueryResultIterator


class QueryResultIterator(BaseQueryResultIterator):
    """
    Iterador para manejar un único resultado de consulta, devolviendo los
    resultados en el formato original sin modificaciones.
    """

    def _format_result(self, query_result):
        """
        Devuelve el resultado de la consulta tal como está.

        Args:
            query_result (dict): Resultado de la consulta en formato de diccionario.

        Returns:
            dict: Resultado de la consulta sin formatear.
        """
        return query_result