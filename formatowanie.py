for x in range(-150, 100, 10):
    print("%-+5i%10i%15i%20s%10.2f" % (x, x ** 2, x ** 3, "Emil", 5.12345))
# %4i%6i%8i robi spacje, .2f zaokrągla do 2 po przecinku
# + dopisuje plus
# - wyrównuje do lewej
# 0 uzupełnia wolne przestrzenie
