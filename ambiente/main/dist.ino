int ultrassonicRead(){
  unsigned long duracao;
  unsigned long distancia;
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  duracao = pulseIn(echo, HIGH);
  distancia = duracao/58;
  
  return distancia;
}
