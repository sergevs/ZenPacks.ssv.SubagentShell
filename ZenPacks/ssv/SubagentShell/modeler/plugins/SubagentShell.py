__doc__="""SubagentShell

maps net-snmp SubagentShell specific templates

$Id: SubagentShell.py,v 1.1 2013/09/05 16:01  Exp $"""

__version__ = '$Revision: 1.1 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class SubagentShell(SnmpPlugin):
    maptype = "SubagentShell"
    relname = "subagentshell"
    compname = "os"
    modname = 'ZenPacks.ssv.SubagentShell.SubagentShell'


    deviceProperties = SnmpPlugin.deviceProperties + ('zDeviceTemplates',)
    mibDesc = {
              '.1.3.6.1.4.1.777.1.1':               'SubagentShell',
              '.1.3.6.1.4.1.777.100.2.1':           'SubagentShellNtpSyncStatus',
              '.1.3.6.1.4.1.777.100.3.1':           'SubagentShellProcStat',
              '.1.3.6.1.4.1.777.100.4.2':           'SubagentShellIpConntrack',
              '.1.3.6.1.4.1.777.100.10.1.1':        'SubagentShellNamedStat',
              '.1.3.6.1.4.1.777.100.11.1':          'SubagentShellMailqLength',
              '.1.3.6.1.4.1.777.100.12.1':          'SubagentShellSwapPages',
    }
    snmpGetMap = GetMap( mibDesc )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.debug(str(self.deviceProperties))
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        rm = self.relMap()


        log.debug('getdata %s mibDesc %s', str(getdata),str(SubagentShell.mibDesc))
        if len(getdata.keys()) == getdata.values().count(None):
          log.info('no data')
          return

        for each in SubagentShell.mibDesc.values():
          if getdata.has_key(each) and getdata[each] != None:
            log.debug('New component/templates append: %s' % each)
            om = self.objectMap({'template_name':each})
            om.title=each
            om.id = each
            rm.append(om)
        return rm
