from pkg_resources import get_distribution

__import__('pkg_resources').declare_namespace(__name__)

__version__ = get_distribution("qamplus").version
__author__ = "QAMplus"
__copyright__ = "Copyright 2017, QAMplus Corp."
__credits__ = ["QAMplus"]
__license__ = "MIT"
__maintainer__ = "QAMplus Corp."
__email__ = "contact@qamplus.com"
__status__ = "Production"