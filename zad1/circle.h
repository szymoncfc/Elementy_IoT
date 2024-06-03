#pragma once

#include "shape.h"

class Circle : public Shape {
private:
    double r;

public:
    Circle();

    double Calculate() override;   
};