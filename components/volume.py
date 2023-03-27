class Volume:
    def __init__(self, volumeLevel=100) -> None:
        """Volume class to control the volume of the media player

        Args:
            volumeLevel (int, optional): Choose the volume level. Defaults to 100.
        """
        self.volumeLevel = volumeLevel
        self.volumeLevelMax = 100
        self.volumeLevelMin = 0

    def setVolumeLevel(self, volumeLevel):
        """Set the volume level

        Args:
            volumeLevel (int): Choose the volume level. Must be between 0 and 100
        """
        if volumeLevel > self.volumeLevelMax:
            volumeLevel = self.volumeLevelMax
        elif volumeLevel < self.volumeLevelMin:
            volumeLevel = self.volumeLevelMin
        self.volumeLevel = volumeLevel
        return self.drawVolume()

    def increaseVolume(self):
        """Increase the volume by 10%. If the volume is already at 100%, it will
        stay at 100%

        Returns:
            str: Return the volume level in dashes
        """
        if self.volumeLevel < self.volumeLevelMax:
            self.volumeLevel += 10
            return self.drawVolume()
        else:
            self.volumeLevel = 100
            return self.drawVolume()

    def decreaseVolume(self):
        """Decrease the volume by 10%. If the volume is already at 0%, it will
        stay at 0%

        Returns:
            str: Return the volume level in dashes
        """
        if self.volumeLevel > self.volumeLevelMin:
            self.volumeLevel -= 10
            return self.drawVolume()
        else:
            self.volumeLevel = 0
            return self.drawVolume()

    def getVolumeLevel(self):
        """Get the volume level

        Returns:
            str: Return the volume level in dashes
        """
        return self.volumeLevel

    def mute(self):
        """Mute the volume

        Returns:
            str: Return the volume level in dashes
        """
        self.volumeLevel = 0
        return self.drawVolume()

    def drawVolume(self):
        """Draw the volume with dashes according to the current volume
        Returns:
            str: Return the volume level in dashes
        """
        volumeLevel = self.getVolumeLevel()
        volumeBars = volumeLevel // 10
        volumeDashes = 10 - volumeBars
        return "Volume: " + "|" + "-" * volumeBars + " " * volumeDashes + "|"
