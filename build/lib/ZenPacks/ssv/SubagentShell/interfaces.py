from Products.Zuul.interfaces import  IComponentInfo
from Products.Zuul.form import schema

class IWebServiceInfo(IComponentInfo):
    """
    Info adapter for LogicalDisk components.
    """
    status = schema.Text(title=u"Status", readonly=True, group='Overview')

