#include <Wire.h> // for I2C
#include <Adafruit_MLX90640.h> // thermal camera libary

//create objects
Adafruit_MLX90640 mlx;
float frame[32 * 24];
String command = "";

//function that takes a single "picture"
void takeSnapshot() {
  //if no picture can be obtained, the failure message prints and then exit the function
  if (mlx.getFrame(frame) != 0) {
    Serial.println("Failed to read frame");
    return;
  }

  for (int y = 0; y < 24; y++) {
    for (int x = 0; x < 32; x++) {
      Serial.print(frame[y * 32 + x], 1);
      if (x < 31) Serial.print(", ");
    }
    Serial.println();
  }
  Serial.println();
}

void setup() {
  //open serial communication
  Serial.begin(115200);
 //delay to let serial connect
delay(10000);

//starts I2C and sets speed at 400kHz
  Wire.begin();
  Wire.setClock(400000);


  if (!mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
    Serial.println("MLX90640 not found. Check wiring and reset");
    while (1) {
      //loop that just lasts forever
      delay(10);
    }
  }

  mlx.setMode(MLX90640_CHESS);
  mlx.setResolution(MLX90640_ADC_18BIT);
  mlx.setRefreshRate(MLX90640_2_HZ);

  Serial.println("Thermal Camera ready. going into main loop");
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n' || c == '\r') {
      command.trim();

      if (command.equals("snap")) {
        takeSnapshot();
      } else if (command.length() > 0) {
        Serial.print("Unknown command: ");
        Serial.println(command);
      }

      command = "";
    } else {
      command += c;
    }
  }
}