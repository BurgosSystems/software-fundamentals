
const int BATHROOM_LIGHT = 11;
const int BEDROOM_LIGHT = 12;
const int KITCHEN_LIGHT = 13;

bool parpadeo = false;
unsigned long tiempoAnterior = 0;
bool estadoParpadeo = false;

bool estadoBathroom = LOW;
bool estadoBedroom = LOW;
bool estadoKitchen = LOW;

void menu(){
   Serial.println("[1]. Turn on bathroom_light");
   Serial.println("[2]. Turn off bathroom_light");
   Serial.println("[3]. Turn on bedroom_light");
   Serial.println("[4]. Turn off bedroom_light");
   Serial.println("[5]. Turn on kitchen_light");
   Serial.println("[6]. Turn off kitchen_light");
   Serial.println("[7]. Turn on all lights");
   Serial.println("[8]. Turn off all lights");
   Serial.println("[9]. Blinking lights");
}

void setup() {
  pinMode(BATHROOM_LIGHT, OUTPUT);
  pinMode(BEDROOM_LIGHT, OUTPUT);
  pinMode(KITCHEN_LIGHT, OUTPUT);
  Serial.begin(9600);
  menu();
}

void loop() {

  unsigned long tiempoActual = millis();

  if (parpadeo == true) {
    if (tiempoActual - tiempoAnterior >= 300) {
      tiempoAnterior = tiempoActual;
      estadoParpadeo = !estadoParpadeo;

      if (estadoBathroom != LOW) digitalWrite(BATHROOM_LIGHT, estadoParpadeo);
      if (estadoBedroom != LOW)  digitalWrite(BEDROOM_LIGHT, estadoParpadeo);
      if (estadoKitchen != LOW)  digitalWrite(KITCHEN_LIGHT, estadoParpadeo);
    }
  }

  if(Serial.available() > 0){
    char opt = Serial.read();

    if (opt != '9') {
      if (opt == '7' || opt == '8') {
        parpadeo = false;
      }
    }

    if (opt == '1'){
      estadoBathroom = HIGH;
      digitalWrite(BATHROOM_LIGHT, HIGH);
    }
    if (opt == '2'){
      estadoBathroom = LOW;
      digitalWrite(BATHROOM_LIGHT, LOW);
    }
    if (opt == '3'){
      estadoBedroom = HIGH;
      digitalWrite(BEDROOM_LIGHT, HIGH);
    }
    if (opt == '4'){
      estadoBedroom = LOW;
      digitalWrite(BEDROOM_LIGHT, LOW);
    }
    if (opt == '5'){
      estadoKitchen = HIGH;
      digitalWrite(KITCHEN_LIGHT, HIGH);
    }
    if (opt == '6'){
      estadoKitchen = LOW;
      digitalWrite(KITCHEN_LIGHT, LOW);
    }

    if (opt == '7'){
      estadoBathroom = HIGH;
      estadoBedroom  = HIGH;
      estadoKitchen  = HIGH;
      digitalWrite(BATHROOM_LIGHT, HIGH);
      digitalWrite(BEDROOM_LIGHT, HIGH);
      digitalWrite(KITCHEN_LIGHT, HIGH);
      parpadeo = false;
    }

    if (opt == '8'){
      estadoBathroom = LOW;
      estadoBedroom  = LOW;
      estadoKitchen  = LOW;
      digitalWrite(BATHROOM_LIGHT, LOW);
      digitalWrite(BEDROOM_LIGHT, LOW);
      digitalWrite(KITCHEN_LIGHT, LOW);
      parpadeo = false;
    }

    if (opt == '9'){
      parpadeo = true;
      estadoBathroom = HIGH;
      estadoBedroom  = HIGH;
      estadoKitchen  = HIGH;
    }
  }
}