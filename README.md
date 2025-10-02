# Ex.05 Design a Website for Server Side Processing
# Date:02-10-2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html>
<head>
    <title>Lamp Power Calculator</title>
</head>
{%load static%}
<body bgcolor="yellow">
    <center>
    <h1 {
font-family:verdana;
style="color:red;"
    }>Power of Lamp Filament</h1>
    <form method="POST">
        {% csrf_token %}
        Intensity (I): <input type="text" name="intensity" value="{{ I }}"><br><br>
        Resistance (R): <input type="text" name="resistance" value="{{ R }}"><br><br>
        <input type="submit" value="Calculate Power">
    </form>

    {% if power %}
        <h2>Power (P) = {{ power }} watts</h2>
    {% endif %}
    </center>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.math)
]

```

  




# SERVER SIDE PROCESSING:
![alt text](<Screenshot (13).png>)
# HOMEPAGE:
![alt text](<Screenshot (12).png>)
# RESULT:
The program for performing server side processing is completed successfully.
