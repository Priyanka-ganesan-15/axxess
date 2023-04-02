// Define LED and force sensor pins
const int LED_PINS[] = {15, 16, 17, 18, 19};
const int FORCE_SENSOR_PINS[] = {A0, A1, A2, A3, A4};
const int NUM_LEDS = 5;

// Define threshold force values (adjust as necessary)
const int THRESHOLD_FORCE = 15;

// Define current LED and force sensor
int currentLED = 0;
int previousLED = 0;

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
  
  // Randomly turn on an LED
  randomSeed(analogRead(0));
  currentLED = random(0, NUM_LEDS);
  digitalWrite(LED_PINS[currentLED], HIGH);
}

void loop() {
  // Read the force sensor value
  int forceValue = analogRead(FORCE_SENSOR_PINS[currentLED]);
  
  // Print the force sensor value to the serial monitor
  Serial.print("Sensor ");
  Serial.print(currentLED);
  Serial.print(": ");
  Serial.println(forceValue);
  
  // If the force value is greater than or equal to the threshold value,
  // turn off the current LED
  if (forceValue >= THRESHOLD_FORCE) {
    digitalWrite(LED_PINS[currentLED], LOW);
    previousLED = currentLED;
    
    // Randomly move to the next LED
    do {
      currentLED = random(0, NUM_LEDS);
    } while (currentLED == previousLED);
    
    // Turn on the next LED
    digitalWrite(LED_PINS[currentLED], HIGH);
    
    // Wait for the corresponding force sensor to be pressed
    while (analogRead(FORCE_SENSOR_PINS[currentLED]) < THRESHOLD_FORCE) {}
  }
  
  // Delay for a short period of time to avoid rapid flickering
delay(50);
}