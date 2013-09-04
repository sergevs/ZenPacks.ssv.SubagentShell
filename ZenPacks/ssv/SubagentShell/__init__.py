import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenRelations.RelSchema import *

OperatingSystem._relations += (("apachestatus", ToManyCont(ToOne, "ZenPacks.ssv.SubagentShell.ApacheStatus", "os")), )
OperatingSystem._relations += (("commandstatus", ToManyCont(ToOne, "ZenPacks.ssv.SubagentShell.CommandStatus", "os")), )
OperatingSystem._relations += (("webservice", ToManyCont(ToOne, "ZenPacks.ssv.SubagentShell.WebService", "os")), )
OperatingSystem._relations += (("pingstatus", ToManyCont(ToOne, "ZenPacks.ssv.SubagentShell.PingStatus", "os")), )

from Products.ZenModel.ZenPack import ZenPackBase
from Products.ZenUtils.ZenScriptBase import ZenScriptBase

class ZenPack(ZenPackBase):
    """ ZenPack loader
    """
    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def remove(self, app, junk):
        ZenPackBase.remove(self, app, junk)
        OperatingSystem._relations = tuple([x for x in OperatingSystem._relations if x[0] not in ['apachestatus','commandstatus','webservice','pingstatus']])
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()
