enum display_mode_name {RTI_RGB, RTI_PAL, RTI_NTSC, RTI_OFF};
const char display_modes[] = {0x40, 0x45, 0x4C, 0x46};
const char brightness_levels[] = {0x20, 0x61, 0x62, 0x23, 0x64, 0x25, 0x26, 0x67, 0x68, 0x29, 0x2A, 0x2C, 0x6B, 0x6D, 0x6E, 0x2F};

int current_display_mode = RTI_NTSC;
bool send_brightness = true;
char current_brightness_level = 13;

//delay between bytes, ms
const int rti_delay = 100;
const int button_pin = A1; // pin for the button
bool display_on = false; // initial state of display

void setup() {
  Serial.begin(2400);
  pinMode(button_pin, INPUT_PULLUP); // set button pin as input with pull-up resistor
  delay(10000); // wait for 10 seconds before starting
}

void loop() {
  if (digitalRead(button_pin) == LOW) { // check if button is pressed
    delay(50); // debounce delay
    if (digitalRead(button_pin) == LOW) { // check again to confirm
      display_on = !display_on; // toggle display state
      while (digitalRead(button_pin) == LOW) {
        // wait for button release to avoid multiple toggles
      }
    }
  }

  if (display_on) {
    rtiWrite(0x46); // code for ON
  } else {
    rtiWrite(0x45); // code for OFF
  }

  rtiWrite(0x20);
  rtiWrite(0x83);

  delay(1000); // delay to prevent too fast sending
}

void rtiWrite(char byte) {
  Serial.write(byte); // changed from Serial.print to Serial.write for correct byte transmission
  delay(rti_delay);
}
