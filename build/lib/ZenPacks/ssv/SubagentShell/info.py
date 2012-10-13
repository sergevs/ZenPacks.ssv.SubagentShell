from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
from ZenPacks.ssv.SubagentShell import interfaces

class WebServiceInfo(ComponentInfo):
    implements(interfaces.IWebServiceInfo)
