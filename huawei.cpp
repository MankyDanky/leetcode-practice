#include <iostream>
#include <vector>

int getCount(const std::vector<std::vector<bool>>& matrix)
{
    throw std::logic_error("Waiting to be implemented");
}

#ifndef RunTests
int main()
{
    std::vector<std::vector<bool>> matrix {
        {false, true, false, false, false},
        {true, false, false, false, false},
        {false, false, false, true, false},
        {false, false, true, false, false},
        {false, false, false, false, false}
    };
    std::cout << getCount(matrix) << std::endl; // should print 6
}
#endif