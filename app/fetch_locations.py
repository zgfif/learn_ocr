import numpy as np
from numpy.typing import NDArray



def fetch_locations(match_map: NDArray[np.floating], threshold: float = 0.99) -> tuple[NDArray[np.intp],NDArray[np.intp]]:
    """
    Extract indexes whose values greater than the threshold.

    Parameters
    ----------
    match_map : NDArray
        array of matching scores in the range [-1, 1].
    threshold : float
        Probability of match (from 0 to 1).

    Returns
    -------
    tuple
        tuple of two NDArrays (rows, columns) which correspond positions of matching elements.
    
    Raises
    ------
    ValueError
        If threshold is not in the range [0, 1].
    """
    if not 0 <= threshold <= 1:
        raise ValueError('Threshold must be in range 0..1')
    rows, cols = np.where(match_map > threshold)
    return rows, cols