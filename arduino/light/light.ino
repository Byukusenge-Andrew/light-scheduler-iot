const int RELAY_PIN = 8; // Relay IN pin
String command;

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH); // Start with relay OFF (Active LOW, light OFF)
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
  Serial.println("Arduino ready");
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.readStringUntil('\n');
    command.trim();
    if (command == "1") {
      digitalWrite(RELAY_PIN, LOW); // Activate relay (Active LOW, light ON)
      Serial.println("Relay ON, Light ON");
    } else if (command == "0") {
      digitalWrite(RELAY_PIN, HIGH); // Deactivate relay (light OFF)
      Serial.println("Relay OFF, Light OFF");
    } else {
      Serial.println("Unknown command: " + command);
    }
  }
}