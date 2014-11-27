__doc__="""SubagentShell DNSLookup

DNSLookup maps net-snmp SubagentShell SUBAGENT-SHELL-DISKSTATS-MIB

$Id: DNSLookup.py,v 1.0 2014/11/27 17:45  Exp $"""

__version__ = '$Revision: 1.0 $'

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.ZenossSecurity import *
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *
import types

class DNSLookup(Service):

  portal_type = meta_type = 'DNSLookup'

  title = ''
  dnsLookupIndex = '0'
  dnsLookupName = ''
  dnsLookupResolvedIp = ''

  _properties = Service._properties + (
      {'id':'dnsLookupName', 'type':'string', 'mode':'r'},
      {'id':'dnsLookupResolvedIp', 'type':'string', 'mode':'r'},
   )

  _relations = Service._relations + (
    ("os", ToOne(ToManyCont,"Products.ZenModel.OperatingSystem","dnslookup")),
  )

  factory_type_information = ( 
    { 
        'id'             : 'DNSLookup',
        'meta_type'      : 'DNSLookup',
        'description'    : """Arbitrary device grouping class""",
        'product'        : 'SubagentShell',
        'immediate_view' : 'DNSLookupDetail',
        'actions'        :
        ( 
            { 'id'            : 'status'
            , 'name'          : 'Status'
            , 'action'        : 'DNSLookupDetail'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'events'
            , 'name'          : 'Events'
            , 'action'        : 'viewEvents'
            , 'permissions'   : (ZEN_VIEW, )
            },
            { 'id'            : 'perfConf'
              , 'name'        : 'Template'
              , 'action'      : 'objTemplates'
              , 'permissions' : ("Change Device", )
            },
            { 'id'            : 'viewHistory'
            , 'name'          : 'Modifications'
            , 'action'        : 'viewHistory'
            , 'permissions'   : (ZEN_VIEW_MODIFICATIONS,)
            },
        )
     },
    )

  security = ClassSecurityInfo()

  def monitored(self):
    """
    Return the monitored status of this component.
  """
    return self.monitor

  def getRRDTemplates(self):
    """
    Return the RRD Templates list
    """
    return [self.getRRDTemplateByName('SubagentShellDNSLookup')]

  def getStatus(self, statClass=None):
    """
    Return the status number for this component.
    """
   # Unknown status if we're not monitoring the interface.
    if self.snmpIgnore():  return -1
    s = self.cacheRRDValue('dnsLookUpExecStatus', -1)
    if type(s) == types.FloatType and s.hex() == 'nan' : return -1
    if s < -1 or s > 0 : s = 1
    return s

  def convertStatus(self, status):
    return {-1:'Unknown',0:'Ok',1:'Failed'}[status]

  # must be to map events to componet
  def viewName(self): 
      """
      Return the component name
      """
      return self.id
  name = viewName

InitializeClass(DNSLookup)
