from src.domain.ComplexNumber import ComplexNumber
from src.services.Service import Service



def test_add():
    service = Service()
    complex_number = ComplexNumber(1, 2)
    service.add(complex_number)
    assert service.get_all()[-1].real == 1
    assert service.get_all()[-1].imaginary == 2
    complex_number = ComplexNumber(3, 4)
    service.add(complex_number)
    assert service.get_all()[-1].real == 3
    assert service.get_all()[-1].imaginary == 4
    print("\033[92mTest passed!\033[0m")