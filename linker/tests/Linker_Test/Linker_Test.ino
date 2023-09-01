void setup() {
  // Note: 115200 has to match with the baud rate of the SerialConnector object
  Serial.begin(115200);
}

void loop() {
  // Repeatedly sends out the UUID properly formatted, then a random extra serial output
  Serial.println("||FS||AE012-01121||");
  Serial.println("This is a test");
  delay(100);
}
