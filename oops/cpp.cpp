#include<iostream>
#include<cstring> // For strcpy
#include<cstdio>  // For printf
using namespace std;

// Base Class
class Car {
// private members are only accessible from within the class
private:
    char* brand;

// public members are accessible from anywhere
public:
    char* model;

    // Constructor to initialize the object
    Car(const char* brand, const char* model) {
        // Allocate memory and copy the string data
        this->brand = new char[strlen(brand) + 1];
        strcpy(this->brand, brand);

        this->model = new char[strlen(model) + 1];
        strcpy(this->model, model);
    }

    // Virtual destructor to ensure proper cleanup in derived classes
    virtual ~Car() {
        // Free the allocated memory
        delete[] brand;
        delete[] model;
    }

    // Getter method to access the private 'brand' member
    const char* getBrand() {
        return this->brand;
    }

    // A 'virtual' function that now prints directly to the console
    virtual void displayCar() {
        printf("%s %s\n", this->brand, this->model);
    }
};

// Derived Class
// ElectricCar inherits publicly from Car
class ElectricCar : public Car {
public:
    char* batterySize;

    // Constructor for ElectricCar
    // It calls the base class (Car) constructor to initialize brand and model
    ElectricCar(const char* batterySize, const char* brand, const char* model) : Car(brand, model) {
        this->batterySize = new char[strlen(batterySize) + 1];
        strcpy(this->batterySize, batterySize);
    }

    // Destructor for ElectricCar
    ~ElectricCar() {
        delete[] batterySize;
    }

    // Overriding the base class's displayCar method
    void displayCar() override {
        // We use the public getter 'getBrand()' because 'brand' is private to Car
        printf("%s %s with a %s battery\n", getBrand(), this->model, this->batterySize);
    }
};

int main(){
    // Create an instance of ElectricCar
    ElectricCar cyberTruck("239kw", "tesla", "s");

    cyberTruck.displayCar();
    printf("%s\n", cyberTruck.getBrand());

    return 0; // Good practice to return 0 from main
};