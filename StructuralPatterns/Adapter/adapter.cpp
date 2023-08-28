#include <iostream>

// Existing interface
class WeatherInCelsius {
public:
    virtual float getTemperature() {
        return 25.0; // returns temperature in Celsius
    }
};

// Third-party library (incompatible interface)
class WeatherInFahrenheit {
public:
    float fetchTemperature() {
        return 77.0; // returns temperature in Fahrenheit
    }
};

// Adapter class
class TemperatureAdapter : public WeatherInCelsius {
private:
    WeatherInFahrenheit* weatherInFahrenheit;
public:
    TemperatureAdapter(WeatherInFahrenheit* weather) : weatherInFahrenheit(weather) {}
    float getTemperature() override {
        float tempFahrenheit = weatherInFahrenheit->fetchTemperature();
        float tempCelsius = (tempFahrenheit - 32) * 5.0 / 9.0;
        return tempCelsius; // Converts Fahrenheit to Celsius
    }
};

// Client code
void displayTemperature(WeatherInCelsius* weatherSource) {
    std::cout << "The current temperature is " << weatherSource->getTemperature() << "°C." << std::endl;
}

int main() {
    // Using the existing interface
    WeatherInCelsius celsiusWeather;
    displayTemperature(&celsiusWeather);

    // Using the third-party library through the adapter
    WeatherInFahrenheit fahrenheitWeather;
    TemperatureAdapter adapter(&fahrenheitWeather);
    displayTemperature(&adapter);

    return 0;
}
