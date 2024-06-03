#include <iostream>
#include <windows.h>
#include <iomanip>
#include "shape.h"

typedef Shape* (*CreateShape)();

int main(){

    HMODULE plugin_circle = LoadLibrary("circle.dll");
    HMODULE plugin_rectangle = LoadLibrary("rectangle.dll");

    if (!plugin_circle) {
        std::cerr << "Error loading dll." << std::endl;
        return 1;
    }

    CreateShape create_circle = reinterpret_cast<CreateShape>(GetProcAddress(plugin_circle, "CreateCircle"));
    if (!create_circle) {
        std::cerr << "Error loading circle." << std::endl;
        return 1;
    }

    CreateShape create_rectangle = reinterpret_cast<CreateShape>(GetProcAddress(plugin_rectangle, "CreateRectangle"));
    if (!create_rectangle) {
        std::cerr << "Error loading rectangle." << std::endl;
        return 1;
    }

    Shape* circle = create_circle();    
    std::cout<< "Circle area: " << std::setprecision(5) << circle->Calculate() << std::endl;

    Shape* rectangle = create_rectangle();    
    std::cout<< "Rectangle area: " << rectangle->Calculate() << std::endl;

    delete circle;
    delete rectangle;

    FreeLibrary(plugin_circle);
    FreeLibrary(plugin_rectangle);
    
    return 0;
}