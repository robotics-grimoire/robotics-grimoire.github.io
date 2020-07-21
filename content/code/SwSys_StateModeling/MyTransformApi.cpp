#include "MyTransformApi.h"

#include <sstream>

MyTransformApi::OutData MyTransformApi::magic(const std::string& buffer)
{
  lastBuf = buffer;
  ++counter;
  std::stringstream sout;
  sout << lastBuf << " [" << counter << "]";
  return sout.str();
}


MyTransformApi::OutData MyTransformApi::extrapolateFromLast()
{
  std::stringstream sout;
  counter+=1001;
  sout << "Extrapolating from past data [" << counter << "]";
  return sout.str();
}
