# VolumeLocker NVDA Add-on
# Toggles a lock for the system volume keys (Up, Down, Mute).
# Created by Adula.

import globalPluginHandler
import ui
import scriptHandler
import addonHandler

# Initialize translation support
try:
    addonHandler.initTranslation()
except:
    pass

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    # Category for Input Gestures dialog
    # Translators: Category name in Input Gestures dialog
    scriptCategory = _("VolumeLocker")
    _locked = False

    @scriptHandler.script(
        # Translators: description for toggle volume lock script in Input Gestures dialog
        description=_("Toggles the volume keys lock."),
        gesture="kb:NVDA+v"
    )
    def script_toggleVolumeLock(self, gesture):
        self._locked = not self._locked
        if self._locked:
            # Translators: Message announced when volume keys are locked
            ui.message(_("Volume locked"))
        else:
            # Translators: Message announced when volume keys are unlocked
            ui.message(_("Volume unlocked"))

    @scriptHandler.script(
        gesture="kb:volumeUp"
    )
    def script_volumeUp(self, gesture):
        if self._locked:
            # Lock is active, consume the key
            return
        # Lock is inactive, pass the key to the system
        gesture.send()

    @scriptHandler.script(
        gesture="kb:volumeDown"
    )
    def script_volumeDown(self, gesture):
        if self._locked:
            # Lock is active, consume the key
            return
        # Lock is inactive, pass the key to the system
        gesture.send()

    @scriptHandler.script(
        gesture="kb:volumeMute"
    )
    def script_volumeMute(self, gesture):
        if self._locked:
            # Lock is active, consume the key
            return
        # Lock is inactive, pass the key to the system
        gesture.send()
