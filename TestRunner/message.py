class ServoPos:
    pan: int
    tilt: int

    def __init__(self, pan, tilt):
        self.pan = int(pan)
        self.tilt = int(tilt)

    def serialize(self):
        return bytes(f"{round(self.pan / 1.5)},{round(self.tilt/1.5)}\n", "utf8")

    @staticmethod
    def measure():
        return ServoPos(300, 300)



class PanelData:
    panel_v: float
    panel_i: float
    panel_p: float

    photo_tr: int
    photo_tl: int
    photo_br: int
    photo_bl: int

    pan: int
    tilt: int

    def deserialize(self, data: bytes):
        data = data.decode("ascii")[:-2]
        data = data[1:]
        panel, photo, servo = data.split("|")

        self.panel_v, self.panel_i, self.panel_p = map(float, panel.split(","))
        self.photo_tr, self.photo_tl, self.photo_br, self.photo_bl = map(int, photo.split(","))
        self.pan, self.tilt = map(int, servo.split(","))
