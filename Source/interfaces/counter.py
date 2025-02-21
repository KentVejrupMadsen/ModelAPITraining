

class Counter:
    def __init__(
        self,
        start_value: int = 0,
        step: int        = 1
    ):
        self.value = start_value
        self.step = step
    
    def getStep(
        self
    ) -> int:
        return self.step
    
    def setStep(
        self, 
        value: int
    ) -> None:
        self.step = value

    def increase(
        self, 
        value: int
    ) -> None:
        self.setValue(
            self.getValue() 
            + 
            value
        )

    def increment(
        self
    ) -> None:
        self.increase(
            self.getStep()
        )
    
    def decrease(
        self, 
        value: int
    ) -> None:
        self.setValue(
            self.getValue() 
            - 
            value
        )
    
    def decrement(
        self
    ) -> None:
        self.decrease(
            self.getStep()
        )

    def getValue(
        self
    ) -> int:
        return self.value
    
    def setValue(
        self, 
        value: int
    ) -> None:
        self.value = value

