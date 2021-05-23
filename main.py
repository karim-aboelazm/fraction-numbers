import decimal
import fractions
from numbers import Rational

# for v in [ decimal.Decimal('0.33333334'),
#            decimal.Decimal('0.34'),
#            decimal.Decimal('0.4'),
#            decimal.Decimal('2.0'),
#            ]:
a = decimal.Decimal('0.33334')
b = decimal.Decimal('0.5')
f =fractions.Fraction.from_decimal(a+b).limit_denominator(10)
print(f)
# print(f.numerator,"/",f.denominator)



