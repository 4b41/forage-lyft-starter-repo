from datetime import datetime
import battery;

class spindler(battery):

    def __init__(self, ld, cd):
        self.last_service_date = ld
        self.current_date = cd
    
    def needs_service(self):
        return (self.current_date - self.last_service_date) > datetime(2);
