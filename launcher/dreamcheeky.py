"""Module to control the Dream Cheeky Original USB Launcher

Example:
    This is a very simple call to move the turret down::

        import usbLauncher.dreamcheeky

        def main():
            laucher = usbLauncher.dreamcheeky.Launcher()
            laucher.setup_launcher()
            laucher.move_down(1000)

        if __name__ == '__main__':
            main()
"""

import time
import hid

class Launcher():
    """Main class. All the magic is here.

    This class uses hidapi to comunicate with the launcher.
    """
    _DOWN = 0x01
    _UP = 0x02
    _LEFT = 0x04
    _RIGHT = 0x08
    _FIRE = 0x10
    _STOP = 0x20

    _DEVICE = None

    def __init__(self):
        """Function to setup the device. Opens the device with
        the magic numbers: 0x0a81, 0x0701
        """
        self._DEVICE = hid.device()
        self._DEVICE.open(0x0a81, 0x0701)

    def info(self):
        """Returns the device informations
        """
        launcher_info = "Manufacturer: %s\n" % self._DEVICE.get_manufacturer_string()
        launcher_info += "Product: %s\n" % self._DEVICE.get_product_string()
        launcher_info += "Serial No: %s\n" % self._DEVICE.get_serial_number_string()
        return launcher_info

    def _send_cmd(self, cmd):
        self._DEVICE.write([0x00, cmd])

    def _send_cmd_with_timer(self, cmd, duration_ms):
        self._send_cmd(cmd)
        time.sleep(duration_ms / 1000.0)
        self._send_cmd(self._STOP)

    def move_up(self, duration=None):
        """Moves the turret up.
        Args:
            duration (optional), mumber of milliseconds to keep moving
        """
        if duration is None:
            self._send_cmd(self._UP)
        else:
            self._send_cmd_with_timer(self._UP, duration)

    def move_down(self, duration=None):
        """Moves the turret down.
        Args:
            duration (optional), mumber of milliseconds to keep moving
        """
        if duration is None:
            self._send_cmd(self._DOWN)
        else:
            self._send_cmd_with_timer(self._DOWN, duration)

    def move_left(self, duration=None):
        """Moves the turret left.
        Args:
            duration (optional), mumber of milliseconds to keep moving
        """
        if duration is None:
            self._send_cmd(self._LEFT)
        else:
            self._send_cmd_with_timer(self._LEFT, duration)

    def move_right(self, duration=None):
        """Moves the turret right.
        Args:
            duration (optional), mumber of milliseconds to keep moving
        """
        if duration is None:
            self._send_cmd(self._RIGHT)
        else:
            self._send_cmd_with_timer(self._RIGHT, duration)

    def stop(self):
        """Stops the current movement.
        """
        self._send_cmd(self._STOP)

    def fire(self, num_shots=1):
        """Fires the missiles
        Args:
            mum_shots (optional value 1), mumber of shots to fire
        """
        if num_shots > 3 or num_shots < 1:
            num_shots = 1
        time.sleep(0.5)
        for i in range(num_shots):
            self._send_cmd(self._FIRE)
            time.sleep(4.5)
    