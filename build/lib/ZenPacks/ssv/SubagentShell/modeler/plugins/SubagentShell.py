__doc__="""SubagentShell

SubagentShell maps SubagentShell specific templates

$Id: SubagentShell.py,v 1.00 2010/11/15 16:01  Exp $"""

__version__ = '$Revision: 1.00 $'

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class SubagentShell(SnmpPlugin):

    deviceProperties = SnmpPlugin.deviceProperties + ('zDeviceTemplates',)
    mibDesc = {
              '.1.3.6.1.4.1.777.1.1':               'SubagentShell',
              '.1.3.6.1.4.1.777.100.2.1':           'SubagentShellNtpSyncStatus',
              '.1.3.6.1.4.1.777.100.3.1':           'SubagentShellProcStat',
              '.1.3.6.1.4.1.777.100.4.2':           'SubagentShellIpConntrack',
              '.1.3.6.1.4.1.777.100.6.2':           'SubagentShellSoftwareLastUpdate',
              '.1.3.6.1.4.1.777.100.10.1.1':        'SubagentShellNamedStat',
              '.1.3.6.1.4.1.777.100.11.1':          'SubagentShellMailqLength',
    }
    snmpGetMap = GetMap( mibDesc )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.debug(str(self.deviceProperties))
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        log.debug(str(device.zDeviceTemplates))

        newTemplates = []
        rmTemplates = []

        log.debug('getdata %s mibDesc %s', str(getdata),str(SubagentShell.mibDesc))
        if len(getdata.keys()) == getdata.values().count(None):
          log.info('no data')
          return

        for each in SubagentShell.mibDesc.values():
          if getdata.has_key(each) and getdata[each] != None:
            newTemplates.append(each)
            log.debug('newTemplates append: %s' % each)
          else:
            rmTemplates.append(each)
            log.debug('rmTemplates append: %s' % each)

        log.info('Current zDeviceTemplaces: %s' % str(device.zDeviceTemplates))

        for each in device.zDeviceTemplates:
          if each not in newTemplates and each not in rmTemplates:
            newTemplates.insert(0,each)
            log.debug('adding to newTemplaces: %s' % str(each))

        device.zDeviceTemplates=sorted(newTemplates)
        log.info('New zDeviceTemplates: %s' %  str(device.zDeviceTemplates))
        om = self.objectMap({'bindTemplates': newTemplates})
        return om
