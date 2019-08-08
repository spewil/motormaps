from sensel import sensel

FRAMERATE = 2000
SCAN_DETAILS = ["High (125Hz)", "Medium (250Hz)", "Low (1000Hz)"]


class SenselException(Exception):
    def __init__(self, message):
        self.message = message


class Morph():
    def __init__(self):
        self.handle = None
        (error, self.device_list) = sensel.getDeviceList()
        if self.device_list.num_devices != 0:
            (error, self.handle) = sensel.openDeviceByID(
                self.device_list.devices[0].idx)
        if self.handle is None:
            raise SenselException(f"Sensel Error: {error}")
        else:
            (error, self.info) = sensel.getSensorInfo(self.handle)
            print(
                f"Device {bytearray(self.device_list.devices[0].serial_num).decode('utf-8')} Found"
            )
            error = sensel.setDynamicBaselineEnabled(self.handle, 0)
            print(f"setDynamicBaselineEnabled False: {error}")
            error, detail = sensel.getScanDetail(self.handle)
            print(f"Scan Detail: {SCAN_DETAILS[detail]}")
            error = sensel.setMaxFrameRate(self.handle, FRAMERATE)
            print(f"setMaxFramerate {FRAMERATE}: {error}")
            error, framerate = sensel.getMaxFrameRate(self.handle)
            print(f"Max Framerate: {framerate}")
            print("Width: " + str(self.info.width) + "mm")
            print("Height: " + str(self.info.height) + "mm")
            self.cols = self.info.num_cols
            self.rows = self.info.num_rows
            print("Cols: " + str(self.cols))
            print("Rows: " + str(self.rows))
            error = sensel.setFrameContent(self.handle,
                                           sensel.FRAME_CONTENT_CONTACTS_MASK)
            print(f"setFrameContent {error}")
            (error, self.frame) = sensel.allocateFrameData(self.handle)
            print(f"allocateFrameData {error}")
            error = sensel.startScanning(self.handle)
            print(f"startScanning {error}")

    def read_frames(self, print=False):
        error = sensel.readSensor(self.handle)
        (error, num_frames) = sensel.getNumAvailableFrames(self.handle)
        frames = []
        for i in range(num_frames):
            error = sensel.getFrame(self.handle, self.frame)
            frames.append(self.frame)
            if print:
                self.print_frames()
        return frames

    def print_frames(self):
        if self.frame.n_contacts > 0:
            print("\nNum Contacts: ", self.frame.n_contacts)
            for n in range(self.frame.n_contacts):
                c = self.frame.contacts[n]
                print("Contact ID: ", c.id)
                if c.state == sensel.CONTACT_START:
                    sensel.setLEDBrightness(self.handle, c.id, 100)
                elif c.state == sensel.CONTACT_END:
                    sensel.setLEDBrightness(self.handle, c.id, 0)

    def close(self):
        error = sensel.freeFrameData(self.handle, self.frame)
        error = sensel.stopScanning(self.handle)
        error = sensel.close(self.handle)
