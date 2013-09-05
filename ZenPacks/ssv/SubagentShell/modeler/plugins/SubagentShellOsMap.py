__doc__="""SubagentShellOsMap

maps net-snmp SubagentShell SUBAGENT-SHELL-OSINFO-MIB to OS model.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
import re

class SubagentShellOsMap(SnmpPlugin):
  """Map mib elements from SubagentShell mib to get os  release. """
  deviceProperties = SnmpPlugin.deviceProperties + ('getOSProductKey',)

  maptype = "SubagentShellOsMap"

  snmpGetMap = GetMap({
      '.1.3.6.1.4.1.777.100.6.1': 'setOSProductKey',
      })

  def process(self, device, results, log):
      """collect snmp information from this device"""
      log.info('processing %s for device %s', self.name(), device.id)
      getdata, tabledata = results
      if getdata['setOSProductKey'] is None: return None
      om = self.objectMap(getdata)
      return om

