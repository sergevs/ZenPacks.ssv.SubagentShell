__doc__="""SubagentShell WebService

WebService maps net-snmp SubagentShell SUBAGENT-SHELL-HTTP-RESPONSE-MIB

$Id: WebService.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.ZenossSecurity import *
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *

class WebService(Service):

  portal_type = meta_type = 'WebService'

  title = ''
  httpRespIndex = '0'
  httpRespCurlArgs = ''

  _properties = Service._properties + (
      {'id':'httpRespCurlArgs', 'type':'string', 'mode':'r'},
   )

  _relations = Service._relations + (
    ("os", ToOne(ToManyCont,"Products.ZenModel.OperatingSystem","webservice")),
  )

  factory_type_information = ( 
    { 
        'id'             : 'WebService',
        'meta_type'      : 'WebService',
        'description'    : """Arbitrary device grouping class""",
        'product'        : 'SubagentShell',
        'immediate_view' : 'WebServiceDetail',
        'actions'        :
        ( 
            { 'id'            : 'status'
            , 'name'          : 'Status'
            , 'action'        : 'WebServiceDetail'
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
    return [self.getRRDTemplateByName('SubagentShellWebService')]

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

InitializeClass(WebService)
