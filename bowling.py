from collections import defaultdict


class BowlingGame():
    def __init__(self):
        self.pins_per_frame = defaultdict(list)
        self.current_frame = 1
        self.current_pins = 10
        self.max_frames = 10
    
    
    @property
    def current_pins(self):
        return self._current_pins
    
    @current_pins.setter
    def current_pins(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        self._current_pins = value

    @current_pins.getter
    def current_pins(self) -> int:
        return self._current_pins


    @property
    def current_frame(self):
        return self._current_frame
    
    @current_frame.setter
    def current_frame(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        self._current_frame = value

    @current_frame.getter
    def current_frame(self) -> int:
        return self._current_frame
    

    def validate_roll(self, roll: int) -> bool:
        standing_pins = self.current_pins - roll
        
        if standing_pins >= 0:
            if standing_pins > self.current_pins:
                raise ValueError("Negative value input is not possible")
            self.current_pins = standing_pins
            return True
        if self.is_game_finished():
            return False
        raise ValueError("Sum of rolls should not be higher than 10")
    

    def bonus_frames(self) -> int:
        last_throw = self.pins_per_frame.get(10)
        if sum(last_throw) != 10:
            return 0
        if len(last_throw) == 2:
            return 1
        return 2


    def is_game_finished(self) -> bool:
        return self.max_frames == self.current_frame
    

    def score(self) -> int:
        total = 0
        for key, value in self.pins_per_frame.items():
            if key > 10:
                break
            if sum(value) == 10:
                if len(value) == 2:
                    total += sum(value) + sum(self.pins_per_frame[key + 1])
                else:
                    total += sum(value) + sum(self.pins_per_frame[key + 1]) + sum(self.pins_per_frame[key + 2])
                continue
            total += sum(value)
        return total
    

    def roll(self, pins_down: int) -> None:
        if self.validate_roll(pins_down):
            if len(self.pins_per_frame[self.current_frame]) < 2:
                self.pins_per_frame[self.current_frame].append(pins_down)
            if pins_down == 10 or len(self.pins_per_frame[self.current_frame]) == 2:
                if self.max_frames == self.current_frame:
                    if self.current_frame == 10:
                        self.max_frames = self.max_frames + self.bonus_frames()
                    else:
                        return                        

                self.current_frame = self.current_frame + 1
                self.current_pins = 10
        else:
            print("Game is finished")
