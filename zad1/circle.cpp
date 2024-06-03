#include "circle.h"
#include <cmath>

Circle::Circle()
{
    r = 2;
}

double Circle::Calculate()
{
    return M_PI * r * r;
}

extern "C" __declspec (dllexport) Shape* CreateCircle()
{

    Circle * module = new Circle();

    return module;
}
