#include <string>

class MyTransformApi
{
public:
  MyTransformApi() = default;
  ~MyTransformApi() = default;

  using OutData=std::string;
  OutData magic(const std::string& buffer);
  OutData extrapolateFromLast();

private:
  std::string lastBuf{};
  unsigned int counter{1000};
};
