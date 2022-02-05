// Testing primeDecomp.h

#include "primeDecomp.h"
#include "test.h"
#include <stdexcept>
#include <map>

using namespace std;

int main(){
    PrimeDecomp obj;
    
    test(obj.factors(2) == "(2)");
    test(obj.factors(5) == "(5)");
    test(obj.factors(7919) == "(7919)");

    test(obj.factors(9015) == "(3)(5)(601)");
    test(obj.factors(55) == "(5)(11)");
    test(obj.factors(9) == "(3**2)");
    test(obj.factors(9074) == "(2)(13)(349)");
    test(obj.factors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)");

}