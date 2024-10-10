class BaseQueryResultIterator():
    """
    ----- CLASE ABSTRACTA -----

    Iterador base para resultados de consultas.

    Esta clase proporciona una implementación básica de iterador para iterar sobre los resultados de una consulta.
    Subclases deben implementar el método `_format_result` para definir cómo se debe formatear cada resultado.

    Atributos:
        __key (str): Una clave del dict dado que cumple que para los valores del dict se puede acceder a cualquier i < len(dict[key]) si no es None.
        __index (int): El índice actual en la iteración.
        __results (dict): Un diccionario que contiene los resultados de la consulta, con listas de valores por clave.
    """

    def __init__(self, results, key):
        """
        Inicializa un iterador de resultados de consulta.

        Args:
            results (dict): Diccionario de resultados de consulta. Debe contener listas 
                            para cada clave, excepto la clave principal que se usa para 
                            la iteración.
            key (str): Clave del diccionario que tiene una lista cuyo len(lista) es equivalente al tamaño de todaas
                            las partes iterables.
        """
        self.__key = key
        self.__index = 0
        self.__results = results
    
    def __next__(self):
        """
        Retorna el siguiente resultado en la iteración.

        Returns:
            formatted dict: Resultado formateado de la consulta.

        Raises:
            StopIteration: Cuando no hay más resultados para iterar.
        """
        if self.__index < len(self.__results[self.__key]):
            query_result = {}
            for key in self.__results.keys():
                query_result[key] = self.__results[key]
                if self.__results[key] is not None:
                    query_result[key] = self.__results[key][self.__index]
            self.__index += 1
            return self._format_result(query_result)
        else:
            raise StopIteration
    
    def _format_result(self, query_result):
        """
        ----- METODO ABSTRACTO -----

        Formatea el resultado de la consulta. Este método debe ser sobrescrito
        por subclases para definir el formato específico del resultado.

        Args:
            query_result (dict): Resultado de la consulta en formato de diccionario.

        Returns:
            formatted dict: Resultado formateado.

        Raises:
            NotImplementedError: Debe ser implementado por subclases.
        """
        raise NotImplementedError("Debe ser implementado por subclases")
