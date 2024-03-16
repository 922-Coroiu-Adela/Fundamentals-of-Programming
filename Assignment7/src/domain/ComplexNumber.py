class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        if self.real == 0:
            return str(self.imaginary) + "i"
        if self.imaginary < 0:
            return str(self.real) + str(self.imaginary) + "i"
        return str(self.real) + "+" + str(self.imaginary) + "i"

    def get_imaginary(self):
        return self.imaginary

    def get_real(self):
        return self.real

    def set_imaginary(self, imaginary):
        self.imaginary = imaginary

    def set_real(self, real):
        self.real = real
