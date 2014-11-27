from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IPingStatusInfo(IComponentInfo):
    host = schema.Entity(title=u"Host", readonly=True, group='Details')
    count = schema.Int(title=u"Ping Count", readonly=True, group='Details')

class IDNSLookupInfo(IComponentInfo):
    lookupName = schema.Entity(title=u"Name", readonly=True, group='Details')
    resolvedIp = schema.Int(title=u"IPs", readonly=True, group='Details')
