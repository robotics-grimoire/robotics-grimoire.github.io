#include "MyOutputApi.h"
#include <cstdlib>
#include <iostream>

/**
 * @brief Sends character stream buffer to next system
 * @param[in] buffer : data buffer that's populated by the system
 * @throws std::exception : Happens when output interface abruptly disconnects.
 */
void MyOutputApi::send(std::string& buffer) noexcept(false)
{
  auto myRandomEffect = rand()%100;
  if(myRandomEffect)
  {
    std::cout << buffer << " --- ";
  }
  else
  {
    throw std::runtime_error("Generic API failure");
  }
}
