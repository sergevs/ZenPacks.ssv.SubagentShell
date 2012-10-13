from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap

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
      om.id = self.prepId("CommandStatus%02d" % int(om.cmdIndex))
      om.snmpindex = int(om.cmdIndex)
      om.title = om.cmdName 
      rm.append(om)
    
    return rm

