// PluginInterface.h
#pragma once

class PluginInterface {
public:
    virtual void performAction() = 0;
    virtual ~PluginInterface() = default;
};

