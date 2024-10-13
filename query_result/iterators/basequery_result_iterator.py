class BaseQueryResultIterator():
    """
    ----- ABSTRACT CLASS -----

    Base iterator for query results.

    This class provides a basic iterator implementation for iterating over the results of a query.
    Subclasses must implement the `_format_result` method to define how each result should be formatted.

    Attributes:
        __key (str): A key from the given dict that ensures that for the values of the dict, any i < len(dict[key]) can be accessed if it is not None.
        __index (int): The current index in the iteration.
        __results (dict): A dictionary that contains the query results, with lists of values by key.
    """

    def __init__(self, results, key):
        """
        Initializes a query result iterator.

        Args:
            results (dict): Dictionary of query results. It must contain lists 
                            for each key, except the main key used for 
                            iteration.
            key (str): Key of the dictionary that has a list whose len(list) is equivalent to the size of all
                    iterable parts.
        """
        self.__key = key
        self.__index = 0
        self.__results = results
    
    def __next__(self):
        """
        Returns the next result in the iteration.

        Returns:
            formatted dict: Formatted query result.

        Raises:
            StopIteration: When there are no more results to iterate.
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
        ----- ABSTRACT METHOD -----

        Formats the query result. This method must be overridden
        by subclasses to define the specific format of the result.

        Args:
            query_result (dict): Query result in dictionary format.

        Returns:
            formatted dict: Formatted result.

        Raises:
            NotImplementedError: Must be implemented by subclasses.
        """
        raise NotImplementedError("Debe ser implementado por subclases")
