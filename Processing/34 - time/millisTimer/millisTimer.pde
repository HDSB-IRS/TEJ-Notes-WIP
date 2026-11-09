int circleX;
int lastTimeDrawn;

void setup(){
  size(400,400);
  circleX = 200;
  lastTimeDrawn = millis();
}

void draw() {
  background(100);  //Clear the screen

  //Change the position of the circle every second
  if (millis() >= lastTimeDrawn + 1000) {
    circleX = (int)random(400);
    lastTimeDrawn = millis();
  }
  
  //Draw the circle
  ellipse(circleX, 200, 20, 20);
  
  
}
