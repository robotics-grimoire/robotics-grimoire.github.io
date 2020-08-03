#include "MyInputApi.h"
#include <cstdlib>

/**
 * @brief Fills the buffer with character stream when information is available
 * @param[in] buffer : data buffer that's populated by the interface
 * @return bool : if TRUE, data was valid. Otherwise an error happened with the input stream.
 */
bool MyInputApi::getNext(std::string& buffer)
{
  auto myRandomEffect = rand()%10;
  buffer.clear();

  if(myRandomEffect)
  {
    buffer = "I got valid data!";
  }

  return myRandomEffect != 0;
}
