__doc__="""SubagentShell CommandStatus 

CommandStatus maps net-snmp SubagentShell SUBAGENT-SHELL-EXEC-COMMAND-MIB 

$Id: CommandStatus.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.ZenossSecurity import *
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *

class CommandStatus(Service):

  portal_type = meta_type = 'CommandStatus'

  title = ''
  cmdIndex = '0'
  cmdName = ''

  _properties = Service._properties + (
      {'id':'cmdName', 'type':'string', 'mode':'r'},
   )

  _relations = Service._relations + (
    ("os", ToOne(ToManyCont,"Products.ZenModel.OperatingSystem","commandstatus")),
  )

  factory_type_information = ( 
    { 
        'id'             : 'CommandStatus',
        'meta_type'      : 'CommandStatus',
        'description'    : """Arbitrary device grouping class""",
        'product'        : 'SubagentShell',
        'immediate_view' : 'CommandStatusDetail',
        'actions'        :
        ( 
            { 'id'            : 'status'
            , 'name'          : 'Status'
            , 'action'        : 'CommandStatusDetail'
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
    return [self.getRRDTemplateByName('SubagentShellCommandStatus')]

  def getStatus(self, statClass=None):
    """
    Return the status number for this component.
    """
   # Unknown status if we're not monitoring the interface.
    if self.snmpIgnore():  return -1
    s = self.cacheRRDValue('cmdExecStatus', None)
    if s is None: s = -1 
    if s != 0: s = 1
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

InitializeClass(CommandStatus)
