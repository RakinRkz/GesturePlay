import platform
# print(platform.system())

from subprocess import call
# val = "150%"


class VolumeController:
    def VolumeChangeBy(value=0):
        volume_value = str(value * 65536)
        call(["amixer", "-D", "pulse", "sset", "Master", volume_value])

#
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = interface.QueryInterface(IAudioEndpointVolume)
# volRange = volume.GetVolumeRange()
#
# volume.SetMasterVolumeLevel(75, None)

