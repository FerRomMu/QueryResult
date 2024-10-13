class BaseQueryResult:
    """
    Base class to represent the result of a query. It handles the 
    initialization of results, representation, and access to elements by index or key.

    Attributes:
        _results (dict): Dictionary of query results.
        _main_key (str): Main key to access the size of non-null results.

    IMPORTANT:
        This class assumes that the results of the ChromaDB query return the "QueryResult" from that library and that
        it has the following structure:
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

    NOTE:
        If ChromaDB changes its return structure in the future, this code may become 
        deprecated and will need updates.
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
        Initializes a query result.

        Args:
            results (dict): Dictionary of query results.
        """
        self._results = results
        self._main_key = 'ids'

    # ---------------------------------------------------------------
    # REPRESENTACION
    # ---------------------------------------------------------------
    def __repr__(self):
        """
        Returns a representation of the query result.

        Returns:
            str: String representation of the results.
        """
        return f"{self.__class__.__name__}:\n{{\n{self._format_results()}\n}}"

    def __str__(self):
        """
        Returns a representation of the query result.

        Returns:
            str: String representation of the results.
        """
        return self.__repr__()

    def _format_results(self):
        # Creates a string representation with line breaks
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
        Selects a function based on the type of argument.

        Args:
            func_num (function): Function to use if the argument is an integer.
            func_str (function): Function to use if the argument is a string.
            args (Array[int or str]): A list of arguments for the function to execute
                                    whose first element is used to determine which function to use.

        Returns:
            Result: The result of the selected function.

        Raises:
            TypeError: If the argument is neither an integer nor a string.
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
        Gets a result based on the numeric index.

        Args:
            index (int): The index of the desired result.

        Returns:
            dict: A dictionary with the results for the specified index.

        Raises:
            IndexError: If the index is out of range for any of the keys.
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
        Gets a result based on the key.

        Args:
            key (str): The key of the desired result.

        Returns:
            list or None: The list of results for the specified key.

        Raises:
            KeyError: If the key is not found in the results.
        """
        if key not in self._results:
            raise KeyError(f"Key '{key}' not found.")
        return self._results[key]
    
    def __getitem__(self, index):
        """
        Gets a result based on the index or the key.

        Args:
            index (int or str): The index or the key of the desired result.

        Returns:
            dict or list or None: The result based on the specified index or key.

        Raises:
            TypeError: If the argument is neither an integer nor a string.
        """
        return self._either_by_type(self._getitem_by_index, self._getitem_by_key, index)