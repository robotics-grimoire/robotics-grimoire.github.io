#include "MyInputApi.h"
#include "MyOutputApi.h"
#include "MyOverseerApi.h"
#include "MyTransformApi.h"

#include <iostream>
#include <cstdlib>

int main(int, char** argv)
{
  MyTransformApi hiddenFunc;
  srand(atoi(argv[1]));
  try
  {
    // Initialize the interfaces
    MyInputApi inputIf;
    inputIf.connect();

    MyOutputApi outputIf;
    outputIf.connect();

    std::string buf;
    while(MyOverseerApi::getInstance().keepRunning())
    {
      // buf.clear();
      MyTransformApi::OutData output;
      auto status = inputIf.getNext(buf);

      if(status)
      {
        // Got new data
        output = hiddenFunc.magic(buf);
      }
      else
      {
        // Data wasn't available
        output = hiddenFunc.extrapolateFromLast();
      }
      outputIf.send(output);
    }
  }
  catch(...)
  {
    std::cout << "Caught an exception, so aborting!" << std::endl;
  }
  return 0;
}
