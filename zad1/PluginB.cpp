// PluginB.cpp
#include "PluginInterface.h"
#include <iostream>


class PluginB : public PluginInterface {
public:
    void performAction() override {
        std::cout << "Plugin B is performing its action." << std::endl;
    }
};