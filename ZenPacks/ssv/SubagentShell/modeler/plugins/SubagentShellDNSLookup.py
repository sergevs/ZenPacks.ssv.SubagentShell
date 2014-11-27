__doc__="""SubagentShell DNSLookup

maps net-snmp SubagentShell SUBAGENT-SHELL-DNSLOOKUP-MIB

$Id: SubagentShellDNSLookup.py,v 1.1 2013/10/07 17:45  Exp $"""

__version__ = '$Revision: 1.0 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from urllib import quote_plus

class SubagentShellDNSLookup(SnmpPlugin):
  """
  Map net-snmp subagent shell DNS lookup status mib to DNSLookup component
  """
  maptype = "DNSLookup"
# both 3 parameters are required 
  relname = "dnslookup"
  compname = "os"
  modname = 'ZenPacks.ssv.SubagentShell.DNSLookup'

  snmpGetTableMaps = (
      GetTableMap('SubagentShellDNSLookup', '.1.3.6.1.4.1.777.100.5.1.1',
              {'.1': 'dnsLookupIndex',
               '.2': 'dnsLookupName',
               '.3': 'dnsLookupResolvedIp',
              }
      ),
  )

  def process(self, device, results, log):
    """collect snmp information from this device"""
    log.info('processing %s for device %s', self.name(), device.id)

    getdata, tabledata = results
    dnsLookupTable = tabledata.get('SubagentShellDNSLookup')
    rm = self.relMap()

    for oid, ds in dnsLookupTable.iteritems():
      om = self.objectMap(ds)
      om.id = self.prepId("SubagentShellDNSLookup-%s" % quote_plus(om.dnsLookupName))
      om.title = om.dnsLookupName
      om.snmpindex = int(om.dnsLookupIndex)
      rm.append(om)
    
    return rm
