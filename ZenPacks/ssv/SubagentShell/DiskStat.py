__doc__="""SubagentShell DiskStat

DiskStat maps net-snmp SubagentShell SUBAGENT-SHELL-DISKSTATS-MIB

$Id: DiskStat.py,v 1.0 2013/10/07 17:45  Exp $"""

__version__ = '$Revision: 1.0 $'

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.ZenossSecurity import *
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *

class DiskStat(Service):

  portal_type = meta_type = 'DiskStat'

  title = ''
  diskStatIndex = '0'
  diskStatDeviceName = ''

  _properties = Service._properties + (
      {'id':'diskStatDeviceName', 'type':'string', 'mode':'r'},
   )

  _relations = Service._relations + (
    ("os", ToOne(ToManyCont,"Products.ZenModel.OperatingSystem","diskstat")),
  )

  factory_type_information = ( 
    { 
        'id'             : 'DiskStat',
        'meta_type'      : 'DiskStat',
        'description'    : """Arbitrary device grouping class""",
        'product'        : 'SubagentShell',
        'immediate_view' : 'DiskStatDetail',
        'actions'        :
        ( 
            { 'id'            : 'status'
            , 'name'          : 'Status'
            , 'action'        : 'DiskStatDetail'
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
    return [self.getRRDTemplateByName('SubagentShellDiskStat')]

  def getStatus(self, statClass=None):
    """
    Return the status number for this component.
    """
   # Unknown status if we're not monitoring the interface.
    if self.snmpIgnore():
            return -1
    return 0

  # must be to map events to componet
  def viewName(self): 
      """
      Return the component name
      """
      return self.id
  name = viewName

InitializeClass(DiskStat)
