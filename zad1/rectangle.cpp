#include "rectangle.h"

Rectangle::Rectangle()
{
    x = 20;
    y = 0.5;
}

double Rectangle::Calculate()
{
    return x*y;
}

extern "C" __declspec (dllexport) Shape* CreateRectangle()
{

    Rectangle * module = new Rectangle();

    return module;
}