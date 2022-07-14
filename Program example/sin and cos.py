import hmath
θ = -1
from time import sleep
print("                                              Sin                                                                                                   Cos")
while True:
    θ += 1
    # Convert frequency to radians and calculate sin and cos.
    sin = hmath.sin(hmath.radian(θ))
    cos = hmath.cos(hmath.radian(θ))
    # Use up to 6 digits after the decimal point for easy viewing.
    new_sin = round(sin * 100000) / 100000
    new_cos = round(cos * 100000) / 100000
    # Align the number of characters for easy viewing.
    new_cos = str(new_cos) + "0" * (7 - len(str(abs(new_cos))))
    new_sin = str(new_sin) + "0" * (7 - len(str(abs(new_sin))))
    if 0 <= cos:
        new_cos = "+" + str(new_cos)
    if 0 <= sin:
        new_sin = "+" + str(new_sin)
    sin_ = round(sin * 40 + 0.5) + 40
    d    = round(cos * 40 + 0.5) + 40
    # display
    print(" " * (10 - len(str(θ))) + str(θ) + "°" + str("===" + "S" * sin_ + "s" * (80 - sin_) + "~~~") + str(new_sin) + "        " + str("C" * d + "c" * (80 - d) + "~~~") + str(new_cos))
    sleep(0.0025)
