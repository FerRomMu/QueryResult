class BaseQueryResult:
    """
    Clase base para representar el resultado de una consulta. Maneja la 
    inicialización de los resultados, la representación y el acceso a los 
    elementos por índice o clave.

    Attributes:
        _results (dict): Diccionario de resultados de consulta.
        _main_key (str): Clave principal para acceder al tamaño de los resultados no nulos.
    
    IMPORTANTE:
        Esta clase asume que los resultados de la query de ChromaDB retornan el "QueryResult" de dicha libreria y que
        tiene la siguiente estructura:
        ids: List[IDs]
        embeddings: Optional[
            Union[
                List[Embeddings],
                List[PyEmbeddings],
                List[NDArray[Union[np.int32, np.float32]]],
            ]
        ]
        documents: Optional[List[List[Document]]]
        uris: Optional[List[List[URI]]]
        data: Optional[List[Loadable]]
        metadatas: Optional[List[List[Metadata]]]
        distances: Optional[List[List[float]]]
        included: Include

    NOTA:
        Si ChromaDB cambia su estructura de retorno en el futuro, este código podría quedar 
        deprecado y necesitará actualizaciones.
    """

    def keys(self):
        return self._results.keys()
    
    def __len__(self):
        return len(self._results[self._main_key])
    # ---------------------------------------------------------------
    # INICIALIZACIÓN
    # ---------------------------------------------------------------
    def __init__(self, results):
        """
        Inicializa un resultado de consulta.

        Args:
            results (dict): Diccionario de resultados de consulta.
        """
        self._results = results
        self._main_key = 'ids'

    # ---------------------------------------------------------------
    # REPRESENTACION
    # ---------------------------------------------------------------
    def __repr__(self):
        """
        Devuelve una representación del query result.

        Returns:
        str: Representación en cadena de los resultados.
        """
        return f"{self.__class__.__name__}:\n{{\n{self._format_results()}\n}}"

    def __str__(self):
        """
        Devuelve una representación del query result.
        
        Returns:
        str: Representación en cadena de los resultados.
        """
        return self.__repr__()

    def _format_results(self):
        # Crea una representación en formato de cadena con saltos de línea
        formatted_results = []
        for key, value in self._results.items():
            if isinstance(value, list):
                value_str = f"[{', '.join(map(str, value))}]"
            elif value is None:
                value_str = "None"
            else:
                value_str = str(value)
            formatted_results.append(f"  '{key}': {value_str}")
        return ",\n".join(formatted_results)
    
    # ---------------------------------------------------------------
    # ACCESO
    # ---------------------------------------------------------------
    def _either_by_type(self, func_num, func_str, *args):
        """
        Selecciona una función basada en el tipo de argumento.

        Args:
            func_num (function): Función a usar si el argumento es un entero.
            func_str (function): Función a usar si el argumento es una cadena.
            args (Array[int or str]): Una lista de argumentos para la función a ejecutar
                                cuyo primer elemento es usado para determinar qué función usar.

        Returns:
            Result: El resultado de la función seleccionada.

        Raises:
            TypeError: Si el argumento no es ni un entero ni una cadena.
        """
        if not args:
            raise ValueError("At least one argument must be provided.")
        
        if isinstance(args[0], int):
            return func_num(*args)
        elif isinstance(args[0], str):
            return func_str(*args)
        else:
            raise TypeError("Index must be either an integer or a string.")
    
    def _getitem_by_index(self, index):
        """
        Obtiene un resultado basado en el índice numerico.

        Args:
            index (int): El índice del resultado deseado.

        Returns:
            dict: Un diccionario con los resultados para el índice especificado.

        Raises:
            IndexError: Si el índice está fuera del rango para alguna de las claves.
        """
        result = {}
        for key in self._results.keys():
            if self._results[key] is not None:
                if index < len(self._results[key]):
                    result[key] = self._results[key][index]
                else:
                    raise IndexError(f"Index {index} out of range for key '{key}'.")
            else:
                result[key] = None
        return result
    
    def _getitem_by_key(self, key):
        """
        Obtiene un resultado basado en la clave.

        Args:
            key (str): La clave del resultado deseado.

        Returns:
            list or None: La lista de resultados para la clave especificada.

        Raises:
            KeyError: Si la clave no se encuentra en los resultados.
        """
        if key not in self._results:
            raise KeyError(f"Key '{key}' not found.")
        return self._results[key]
    
    def __getitem__(self, index):
        """
        Obtiene un resultado basado en el índice o la clave.

        Args:
            index (int or str): El índice o la clave del resultado deseado.

        Returns:
            dict or list or None: El resultado basado en el índice o la clave especificada.

        Raises:
            TypeError: Si el argumento no es un entero ni una cadena.
        """
        return self._either_by_type(self._getitem_by_index, self._getitem_by_key, index)