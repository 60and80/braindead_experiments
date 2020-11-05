#include <iostream>
#include <windows.h>
#include <tchar.h>

//Simple program that runs auxiliary.cpp
int main() {
    std::cout << "MAIN\n";

    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory( &si, sizeof(si) );
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi) );

    CreateProcess( nullptr,   // Runs second program!
                   const_cast<char *>("part1_auxiliary"),
                   nullptr,
                   nullptr,
                   FALSE,
                   0,
                   nullptr,
                   nullptr,
                   &si,
                   &pi );

}
