// MainProgram.cpp
#include <iostream>
#include <windows.h>

typedef void (__stdcall *perform)();

int main() {
    HMODULE pluginHandleA = LoadLibraryA("plugina.dll");
    HMODULE pluginHandleB = LoadLibraryA("pluginb.dll");

    if (!pluginHandleA || !pluginHandleB) {
        std::cerr << "Error loading plug-ins." << std::endl;
        return 1;
    }

    // Get function pointers for the performAction() method
    auto performActionA = reinterpret_cast<void (*)()>(GetProcAddress(pluginHandleA, "performAction"));
    auto performActionB = reinterpret_cast<void (*)()>(GetProcAddress(pluginHandleB, "performAction"));
    perform myFunction = (perform)GetProcAddress(pluginHandleA, "performAction");

    /// FARPROC myFunction = GetProcAddress(hModule, "myFunction");
    ///if (myFunction) {
        ///((void (*)())myFunction)();
        //std::cout<<"A"<< std::endl;
    //}

    if (!myFunction) {
        std::cout << "Could not locate the function" << std::endl;
        return EXIT_FAILURE;
    }

    myFunction();


    // Call the plug-in methods
    performActionA();
    performActionB();

    // Clean up
    FreeLibrary(pluginHandleA);
    FreeLibrary(pluginHandleB);

    return 0;
}