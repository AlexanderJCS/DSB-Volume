"""
:author: Alexander Castronovo
:organization: Max Planck Florida Institute for Neuroscience
:date: Apr 15 2025 12:37
:dragonflyVersion: 2024.1.0.1601
:UUID: efd060071a1711f0b40cf83441a96bd5
"""

__version__ = '1.0.0'

from ORSServiceClass.OrsPlugin.orsPlugin import OrsPlugin
from ORSServiceClass.OrsPlugin.uidescriptor import UIDescriptor
from ORSServiceClass.actionAndMenu.menu import Menu
from ORSServiceClass.decorators.infrastructure import menuItem


class DSB_Volume_045f5ca4127611f1bb63e0d55e2bb93d(OrsPlugin):

    # Plugin definition
    multiple = True
    savable = False
    keepAlive = False
    canBeGenericallyOpened = False

    # UIs
    UIDescriptors = [UIDescriptor(name='MainFormDsbVolume',
                                  title='DSB Volume',
                                  dock='Floating',
                                  tab='Main',
                                  modal=False,
                                  collapsible=True,
                                  floatable=True)]

    def __init__(self, varname=None):
        super().__init__(varname)

    @classmethod
    def getMainFormName(cls):
        return 'MainFormDsb'

    @classmethod
    def getMainFormClass(cls):
        from .mainformdsb import MainFormDsb
        return MainFormDsb

    @classmethod
    def openGUI(cls):
        instance = DSB_Volume_045f5ca4127611f1bb63e0d55e2bb93d()

        if instance is not None:
            instance.openWidget("MainFormDsbVolume")

    @classmethod
    @menuItem("Plugins")
    def DSB(cls):
        menu_item = Menu(title="Start DSB Volume",
                         id_="DSB_Volume_045f5ca4127611f1bb63e0d55e2bb93d",
                         section="",
                         action="DSB_Volume_045f5ca4127611f1bb63e0d55e2bb93d.openGUI()")

        return menu_item
