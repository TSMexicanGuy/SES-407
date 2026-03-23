#include <Wire.h>
#include <Adafruit_MLX90640.h>

Adafruit_MLX90640 mlx;
float frame[32 * 24];

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(10);
  }

  Wire.begin();
  Wire.setClock(400000);

  Serial.println("MLX90640 test");

  if (!mlx.begin(MLX90640_I2CADDR_DEFAULT, &Wire)) {
    Serial.println("Could not find MLX90640. Check wiring.");
    while (1) {
      delay(10);
    }
  }

  Serial.println("MLX90640 found!");

  mlx.setMode(MLX90640_CHESS);
  mlx.setResolution(MLX90640_ADC_18BIT);
  mlx.setRefreshRate(MLX90640_2_HZ);
}

void loop() {
  if (mlx.getFrame(frame) != 0) {
    Serial.println("Failed to read frame");
    delay(500);
    return;
  }

  Serial.println("Frame:");

  for (int y = 0; y < 24; y++) {
    for (int x = 0; x < 32; x++) {
      Serial.print(frame[y * 32 + x], 1);
      Serial.print("\t");
    }
    Serial.println();
  }

  Serial.println();
  delay(1000);
}