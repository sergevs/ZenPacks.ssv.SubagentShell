__doc__="""SubagentShell ApacheStatus

maps net-snmp SubagentShell SUBAGENT-SHELL-APACHE-STATUS-MIB

$Id: SubagentShellApacheStatus.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

class SubagentShellApacheStatus(SnmpPlugin):
  """
  Map net-snmp subagent shell apache status mib to ApacheStatus component
  """
  maptype = "ApacheStatus"
# both 3 parameters are required 
  relname = "apachestatus"
  compname = "os"
  modname = 'ZenPacks.ssv.SubagentShell.ApacheStatus'

  snmpGetTableMaps = (
      GetTableMap('SubagentShellApacheStatus', '.1.3.6.1.4.1.777.100.1.1.1',
              {'.1':  'apsIndex',
               '.17': 'apsUrl',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    apacheStatusTable = tabledata.get('SubagentShellApacheStatus')
    rm = self.relMap()

    for oid, aps in apacheStatusTable.iteritems():
      om = self.objectMap(aps)
      om.id = self.prepId("SubagentShellApacheStatus%02d" % int(om.apsIndex))
      om.title = om.apsUrl
      om.snmpindex = int(om.apsIndex)
      rm.append(om)
    
    return rm

