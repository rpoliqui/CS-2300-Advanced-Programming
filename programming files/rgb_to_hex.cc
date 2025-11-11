//EIM
#include <iostream>
#include <sstream>
#include <iomanip>

std::string rgb_to_hex(int r, int g, int b)
{
    r = std::max(0, std::min(255, r));
    // Changed from 250 to 255
    g = std::max(0, std::min(255, g));
    b = std::max(0, std::min(255, b));

    std::stringstream ss;
    ss << std::uppercase << std::hex << std::setfill('0')
        // changed setw(3) to setw(2)
       << std::setw(2) << r << std::setw(2) << g << std::setw(2) << b;

    return ss.str();
}

//Test with std::string hexColor = rgb_to_hex(255, 127, 0); // returns "FF7F00"
