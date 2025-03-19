import pygame

class DataInfo:
    def __init__(self, surface, font, dataFile, time):
        self.surface = surface
        self.font = font
        self.dataFile = dataFile
        self.time = time
        self.menuNum = 0
        self.hasData = False

    def update_data(self):
        self.hasData = bool(self.dataFile.data)

    def menu(self):
        self.surface.fill('white')
        if self.hasData:
            information = self.dataFile.data.get(f"{self.menuNum}", {})
            y_offset = 50
            self.surface.blit(self.font.render(f"Time: {self.menuNum}", True, (0, 0, 0)), (50, y_offset))
            y_offset += 40
            if "plant" in information:
                self.surface.blit(self.font.render("Planted Crops:", True, (0, 0, 0)), (50, y_offset))
                y_offset += 30
                for crop, amount in information["plant"].items():
                    self.surface.blit(self.font.render(f"{crop}: {amount}", True, (0, 0, 0)), (50, y_offset))
                    y_offset += 30
            if "harvest" in information:
                self.surface.blit(self.font.render("Harvested Crops:", True, (0, 0, 0)), (50, y_offset))
                y_offset += 30
                for crop, amount in information["harvest"].items():
                    if crop != "money":
                        self.surface.blit(self.font.render(f"{crop}: {amount}", True, (0, 0, 0)), (50, y_offset))
                        y_offset += 30
                self.surface.blit(self.font.render(f"Money: {information['harvest']['money']}", True, (0, 0, 0)), (50, y_offset))
                y_offset += 30
                self.surface.blit(self.font.render(f"Total Money: {self.dataFile.data.get('total_money', 0)}", True, (0, 0, 0)), (50, y_offset))