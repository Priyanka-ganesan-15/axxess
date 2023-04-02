// Define LED and force sensor pins
const int LED_PINS[] = {15, 16, 17, 18, 19};
const int FORCE_SENSOR_PINS[] = {A0, A1, A2, A3, A4};
const int NUM_LEDS = 5;

// Define threshold force values (adjust as necessary)
const int THRESHOLD_FORCE = 15;

// Define current LED and force sensor
int currentLED = 0;
int currentSensor = 0;

int counter = 0; // Counter variable to keep track of iterations

void setup() {
  // Set LED pins as outputs
  for (int i = 0; i < NUM_LEDS; i++) {
    pinMode(LED_PINS[i], OUTPUT);
  }
  
  // Set force sensor pins as inputs
  for (int i = 0; i < NUM_LEDS; i++) {
    pinMode(FORCE_SENSOR_PINS[i], INPUT);
  }
  
  // Initialize serial communication
  Serial.begin(9600);
  
  // Turn on the first LED
  digitalWrite(LED_PINS[currentLED], HIGH);
}

void loop() {
  if (counter < 8) { // Check if the counter is less than 5
    // Read the force sensor value
    int forceValue = analogRead(FORCE_SENSOR_PINS[currentSensor]);
    
    // Print the force sensor value to the serial monitor
    Serial.print("Sensor ");
    Serial.print(currentSensor);
    Serial.print(": ");
    Serial.println(forceValue);
    
    // If the force value is greater than or equal to the threshold value,
    // turn off the LED
    if (forceValue >= THRESHOLD_FORCE) {
      digitalWrite(LED_PINS[currentLED], LOW);
      
      // Increment the LED and force sensor indices
      currentLED = (currentLED + 1) % NUM_LEDS;
      currentSensor = (currentSensor + 1) % NUM_LEDS;
      
      // Turn on the next LED
      digitalWrite(LED_PINS[currentLED], HIGH);
      
      counter++; // Increment the counter variable
    }
    
    // Delay for a short period of time to avoid rapid flickering
    delay(50);
  }
}