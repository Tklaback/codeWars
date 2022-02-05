#ifndef TEST_H
#define TEST_H
#include <iostream>

// Unit test set up

namespace {
    void do_test(const char* text, bool cond){
        if (!cond){
            std::cout << "FAILED" << std::endl;
        }
        else{
            std::cout << "PASSED" << std::endl;
        }
    }
}

#define test(cond) do_test(#cond, cond)


#endif