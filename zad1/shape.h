#pragma once

class Shape {
public:
    virtual double Calculate() = 0;
    virtual ~Shape() = default;
};
