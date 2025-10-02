from django.shortcuts import render

def math(request):
    power = None
    I = ''
    R = ''

    if request.method == "POST":
        try:
            I = float(request.POST.get("intensity", 0))
            R = float(request.POST.get("resistance", 0))
            # Formula: P = I^2 * R
            power = (I ** 2) * R
        except:
            power = "Invalid input!"

    return render(request, "math.html", {
        "I": I,
        "R": R,
        "power": power
    })
