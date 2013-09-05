__doc__="""SubagentShell WebService

maps net-snmp SubagentShell SUBAGENT-SHELL-HTTP-RESPONSE-MIB

$Id: SubagentShellWebService.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

class SubagentShellWebService(SnmpPlugin):
  """
  Map net-snmp subagent shell apache status mib to WebService component
  """
  maptype = "WebService"
# both 3 parameters are required 
  relname = "webservice"
  compname = "os"
  modname = 'ZenPacks.ssv.SubagentShell.WebService'

  snmpGetTableMaps = (
      GetTableMap('SubagentShellWebService', '.1.3.6.1.4.1.777.100.8.1.1',
              {'.1': 'httpRespIndex',
               '.6': 'httpRespCurlArgs',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    webServiceTable = tabledata.get('SubagentShellWebService')
    rm = self.relMap()

    for oid, ws in webServiceTable.iteritems():
      om = self.objectMap(ws)
      om.id = self.prepId("WebService%02d" % int(om.httpRespIndex))
      om.snmpindex = int(om.httpRespIndex)
      om.title = om.httpRespCurlArgs 
      rm.append(om)
    
    return rm

