import Enum

class FrequencyCode(str, Enum):
    """Frequency codes for specifying the NIPA table release frequency."""

    M = "M"
    Q = "Q"
    A = "A"
    
class ShowMillionsFlag(str, Enum):
    """
    Flag for specifying whether raw or million-dollar data should be 
    returned. Can be used when requesting percent tables; however, it will
    have no impact on the data values. Default is 'N'.
    """

    N = "N"
    Y = "Y"