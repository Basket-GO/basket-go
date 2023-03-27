class Volume:
    def __init__(self, volumeLevel=100) -> None:
        self.volumeLevel = volumeLevel
        self.volumeLevelMax = 100
        self.volumeLevelMin = 0

    def setVolumeLevel(self, volumeLevel):
        """
        Set the volume level to the specified value
        """
        if volumeLevel > self.volumeLevelMax:
            volumeLevel = self.volumeLevelMax
        elif volumeLevel < self.volumeLevelMin:
            volumeLevel = self.volumeLevelMin
        self.volumeLevel = volumeLevel
        return self.drawVolume()

    def increaseVolume(self):
        if self.volumeLevel < self.volumeLevelMax:
            self.volumeLevel += 10
            return self.drawVolume()
        else:
            self.volumeLevel = 100
            return self.drawVolume()

    def decreaseVolume(self):
        if self.volumeLevel > self.volumeLevelMin:
            self.volumeLevel -= 10
            return self.drawVolume()
        else:
            self.volumeLevel = 0
            return self.drawVolume()

    def getVolumeLevel(self):
        return self.volumeLevel

    def mute(self):
        self.volumeLevel = 0
        return self.drawVolume()

    def drawVolume(self):
        """Draw the volume with dashes according to the current volume
        level. 1 bar corresponds to 10%. When the volume is full, there are 10 bars
        """
        volumeLevel = self.getVolumeLevel()
        volumeBars = volumeLevel // 10
        volumeDashes = 10 - volumeBars
        return "Volume: " + "|" + "-" * volumeBars + " " * volumeDashes + "|"
