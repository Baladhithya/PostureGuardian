#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

void setup(void) {
  Serial.begin(115200);
  while (!Serial);

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.print("AccelX:"); Serial.print(a.acceleration.x); Serial.print(",");
  Serial.print("AccelY:"); Serial.print(a.acceleration.y); Serial.print(",");
  Serial.print("AccelZ:"); Serial.print(a.acceleration.z); Serial.print(",");
  Serial.print("GyroX:"); Serial.print(g.gyro.x); Serial.print(",");
  Serial.print("GyroY:"); Serial.print(g.gyro.y); Serial.print(",");
  Serial.print("GyroZ:"); Serial.println(g.gyro.z);

  delay(200);
}
