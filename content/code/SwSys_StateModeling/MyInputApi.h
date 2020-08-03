#include <string>

class MyInputApi
{
public:
  // Constructors, Assignments, & Destructor
  MyInputApi() = default;
  MyInputApi(const MyInputApi&) = default;
  MyInputApi(MyInputApi&&) = delete;
  MyInputApi& operator=(const MyInputApi&) = default;
  MyInputApi& operator=(MyInputApi&&) = delete;
  ~MyInputApi() = default;

  // Public methods

  /**
   * @brief Simulated connection function call
   */
  void connect() {}

  /**
   * @brief Fills the buffer with character stream when information is available
   * @param[in] buffer : data buffer that's populated by the interface
   * @return bool : if TRUE, data was valid. Otherwise an error happened with the input stream.
   */
  bool getNext(std::string& buffer);

};
