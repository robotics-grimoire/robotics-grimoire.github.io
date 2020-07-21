#include <string>
#include <stdexcept>

class MyOutputApi
{
public:
  // Constructors, Assignments, & Destructor
  MyOutputApi() = default;
  MyOutputApi(const MyOutputApi&) = default;
  MyOutputApi(MyOutputApi&&) = delete;
  MyOutputApi& operator=(const MyOutputApi&) = default;
  MyOutputApi& operator=(MyOutputApi&&) = delete;
  ~MyOutputApi() = default;

  // Public methods

  /**
   * @brief Simulated connection function call
   */
  void connect() {}
  
  /**
   * @brief Sends character stream buffer to next system
   * @param[in] buffer : data buffer that's populated by the system
   * @throws std::exception : Happens when output interface abruptly disconnects.
   */
  void send(std::string& buffer) noexcept(false);
};
