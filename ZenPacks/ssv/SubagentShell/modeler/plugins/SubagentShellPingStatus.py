__doc__="""SubagentShell PingStatus 

maps net-snmp SubagentShell SUBAGENT-SHELL-PING-STAT-MIB

$Id: SubagentShellPingStatus.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

class SubagentShellPingStatus(SnmpPlugin):
  """
  Map net-snmp subagent shell ping status mib to PingStatus component
  """
  maptype = "PingStatus"
# both 3 parameters are required 
  relname = "pingstatus"
  compname = "os"
  modname = 'ZenPacks.ssv.SubagentShell.PingStatus'

  snmpGetTableMaps = (
      GetTableMap('SubagentShellPingStatus', '.1.3.6.1.4.1.777.100.13.1.1',
              {'.1': 'pingIndex',
               '.2': 'pingHost',
               '.3': 'pingTransmitted',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    pingStatusTable = tabledata.get('SubagentShellPingStatus')
    rm = self.relMap()

    for oid, aps in pingStatusTable.iteritems():
      om = self.objectMap(aps)
      om.id = self.prepId("SubagentShellPingStatus%02d" % int(om.pingIndex))
      om.title = om.pingHost
      om.pingCount = int(om.pingTransmitted)
      om.snmpindex = int(om.pingIndex)
      log.debug("pingTransmitted %s" , om.pingTransmitted )
      rm.append(om)
    
    return rm

