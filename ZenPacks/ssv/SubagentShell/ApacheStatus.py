from Globals import InitializeClass

from AccessControl import ClassSecurityInfo

from Products.ZenModel.ZenossSecurity import *

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *

class ApacheStatus(Service):

  portal_type = meta_type = 'ApacheStatus'

  title = ''
  apsIndex = '0'
  apsUrl = ''

  _properties = Service._properties + (
      {'id':'apsUrl', 'type':'string', 'mode':'r'},
   )

  _relations = Service._relations + (
    ("os", ToOne(ToManyCont,"Products.ZenModel.OperatingSystem","apachestatus")),
  )

  factory_type_information = ( 
    { 
        'id'             : 'ApacheStatus',
        'meta_type'      : 'ApacheStatus',
        'description'    : """Arbitrary device grouping class""",
        'product'        : 'SubagentShell',
        'immediate_view' : 'ApacheStatusDetail',
        'actions'        :
        ( 
            { 'id'            : 'status'
            , 'name'          : 'Status'
            , 'action'        : 'ApacheStatusDetail'
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
    return [self.getRRDTemplateByName('SubagentShellApacheStatus')]

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

InitializeClass(ApacheStatus)
