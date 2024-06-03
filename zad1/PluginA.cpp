// PluginA.cpp
#include "PluginInterface.h"
#include <iostream>


class PluginA : public PluginInterface {
public:
    __declspec(dllexport) void performAction() override {
        std::cout << "Plugin A is performing its action." << std::endl;
    }
};

//extern "C" {
//    __declspec(dllexport) PluginA;
//}
