import pytest
from index import *

@pytest.mark.parametrize(
        "inputtext, expected",
        [
            ("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00" , ("RENE" , 215.0)),
            ("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00" , ("RENE" , 215.6)),
            ("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-00:00" , ("RENE" , 290.0)),
            ("ASTRID=MO10:00-12:00,TH12:00-14:00,SU20s:00-21:00" , ("ASTRID" , 85)),
            ("ASTRIDMO10:00-12:00,TH12:00-14:00,SU20s:00-21:00" , ("ASTRID" , 85)),
            ("" , ("ASTRID" , 85)),
            ("ASTRID=MO10:00-12:00,TH12:00-14:00,SU24:00-24:00" , ("ASTRID" , 85)),
            ("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-25:00" , ("RENE" , 215)),
            ("ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00" , ("ASTRID" , 85))
        ]
    )

def test_calculate(inputtext , expected):
    pay = Payment(inputtext)
    assert pay.calculate() == expected
    
    