class MyOverseerApi
{
public:
  static MyOverseerApi& getInstance()
  {
    static MyOverseerApi instance;
    return instance;
  }

  bool keepRunning()
  {
    counter++;
    return 100 > counter;
  }

private:
  unsigned int counter{0};

  MyOverseerApi() = default;
  MyOverseerApi(const MyOverseerApi&) = delete;
  MyOverseerApi(MyOverseerApi&&) = delete;
  MyOverseerApi& operator=(const MyOverseerApi&) = delete;
  MyOverseerApi& operator=(MyOverseerApi&&) = delete;
  ~MyOverseerApi() = default;
};
