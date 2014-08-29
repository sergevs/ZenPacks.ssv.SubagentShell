__doc__="""SubagentShell CommandStatus 

maps net-snmp SubagentShell SUBAGENT-SHELL-EXEC-COMMAND-MIB 

$Id: SubagentShellCommandStatus.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from urllib import quote_plus

class SubagentShellCommandStatus(SnmpPlugin):
  """
  Map net-snmp subagent shell apache status mib to CommandStatus component
  """
  maptype = "CommandStatus"
# both 3 parameters are required 
  relname = "commandstatus"
  compname = "os"
  modname = 'ZenPacks.ssv.SubagentShell.CommandStatus'

  snmpGetTableMaps = (
      GetTableMap('SubagentShellCommandStatus', '.1.3.6.1.4.1.777.100.9.1.1',
              {'.1': 'cmdIndex',
               '.5': 'cmdName',
               '.7': 'cmdMonitoringTemplate',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    commandStatusTable = tabledata.get('SubagentShellCommandStatus')
    rm = self.relMap()

    for oid, cs in commandStatusTable.iteritems():
      om = self.objectMap(cs)
      om.id = self.prepId("CommandStatus-%s" % quote_plus(om.cmdName))
      om.snmpindex = int(om.cmdIndex)
      om.title = om.cmdName 
      rm.append(om)
    
    return rm

