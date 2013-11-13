__doc__="""SubagentShell DiskStat

maps net-snmp SubagentShell SUBAGENT-SHELL-DISKSTATS-MIB

$Id: SubagentShellDiskStat.py,v 1.1 2013/10/07 17:45  Exp $"""

__version__ = '$Revision: 1.0 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

class SubagentShellDiskStat(SnmpPlugin):
  """
  Map net-snmp subagent shell apache status mib to DiskStat component
  """
  maptype = "DiskStat"
# both 3 parameters are required 
  relname = "diskstat"
  compname = "os"
  modname = 'ZenPacks.ssv.SubagentShell.DiskStat'

  snmpGetTableMaps = (
      GetTableMap('SubagentShellDiskStat', '.1.3.6.1.4.1.777.100.14.3.1',
              {'.1': 'diskStatIndex',
               '.2': 'diskStatDeviceName',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    diskStatTable = tabledata.get('SubagentShellDiskStat')
    rm = self.relMap()

    for oid, ds in diskStatTable.iteritems():
      om = self.objectMap(ds)
      om.id = self.prepId("SubagentShellDiskStat%02d" % int(om.diskStatIndex))
      om.title = om.diskStatDeviceName
      om.snmpindex = int(om.diskStatIndex)
      rm.append(om)
    
    return rm

