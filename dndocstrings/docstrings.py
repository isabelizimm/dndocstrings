def numpy_scipy(a: str, b: int):
    """An example of numpy or scipy docstring

    Parameters
    ----------
    a : str
        Description of parameter a
    b : int
        Description of parameter b
    c : str
        there's actually no c. you can lie in docstrings
    
    Returns
    -------
    int
        Description of anonymous integer return value.
    
    Notes
    -----
    This is what a note might look like.

    Example
    -------
    >>> 1 + 1
    """
    return a, b

def numpy_scipy_no_types(a, b):
    """An example of numpy or scipy docstring

    Parameters
    ----------
    a :
        Description of parameter a
    b :
        Description of parameter b
    c :
        there's actually no c. you can lie in docstrings
    
    Returns
    -------
    int
        Description of anonymous integer return value.
    
    Notes
    -----
    This is what a note might look like.

    Example
    -------
    >>> 1 + 1
    """
    return a, b

def google(a: str, b: int):
    """Example of google docstring.

    There might even be a longer description here!

    Args:
      a: this is the first param
      b: this is the second param
    
    Returns:
      The key to life
    """
    return a, b

def epytext(a: str, b: int):
    """Example of epytext docstring.

    This is a paragraph.

    @param a: This is a description of
        the parameter a to a function.
        Note that the description is
        indented four spaces.
    @type a: str
    @param b: this is a second param
    @type b: int
    
    @return: this function returns something for sure
    @rtype str
    """
    return a, b

def rest(a: str, b: int):
    """
    This is a reST style.

    :param a: this is a first param
    :param b: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    return a, b