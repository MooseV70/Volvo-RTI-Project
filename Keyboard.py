#include <Keyboard.h>

const int rows = 6; // Number of rows
const int cols = 3; // Number of columns

// Pin definitions for rows and columns
int rowPins[rows] = {9, 8, 7, 6, 4, 3};
int colPins[cols] = {13, 12, 11};

// Character mapping corresponding to the pressed pin combinations
char keymap[rows][cols] = {
  {KEY_RETURN, KEY_ESC, 'O'},   // Use KEY_RETURN for Enter key
  {'V', 'N', 'H'},
  {'1', '2', KEY_DOWN_ARROW},   // Use KEY_DOWN_ARROW for Down arrow key
  {'X', 'C', KEY_UP_ARROW},     // Use KEY_UP_ARROW for Up arrow key
  {'D', 'E', 'F'},
  {'G', 'I', 'M'}
};

bool keyPressed = false; // Indicates if a key is currently being pressed
unsigned long lastKeyPressTime = 0;
const unsigned long debounceDelay = 50;

void setup() {
  Keyboard.begin(); // Initialize keyboard emulation
}

void loop() {
  char key = getKeyWithDebounce();
  
  if (key != '\0' && !keyPressed) {
    keyPressed = true; // Set key pressed flag
    
    // Simulate key press for other keys
    Keyboard.write(key);
    
    delay(50); // Delay for stability
  }
  
  // Reset key pressed flag after key is released
  if (keyPressed && key == '\0') {
    keyPressed = false;
  }
}

char getKeyWithDebounce() {
  unsigned long currentMillis = millis();
  if (currentMillis - lastKeyPressTime >= debounceDelay) {
    lastKeyPressTime = currentMillis;

    // Scan rows
    for (int i = 0; i < rows; i++) {
      pinMode(rowPins[i], OUTPUT);
      digitalWrite(rowPins[i], LOW);

      // Scan columns
      for (int j = 0; j < cols; j++) {
        pinMode(colPins[j], INPUT_PULLUP);
        if (digitalRead(colPins[j]) == LOW) {
          // Return the corresponding character
          delay(50); // Delay for debounce
          if (digitalRead(colPins[j]) == LOW) {
            return keymap[i][j];
          }
        }
        pinMode(colPins[j], OUTPUT);
        digitalWrite(colPins[j], HIGH);
      }

      pinMode(rowPins[i], INPUT); // Set the row pin back to input
    }
  }
  
  return '\0'; // No key pressed
}
