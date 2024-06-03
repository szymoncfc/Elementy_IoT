#pragma once

#include "shape.h"

class Rectangle : public Shape{

private:
    double x;
    double y;

public:
    Rectangle();

    double Calculate() override;

};