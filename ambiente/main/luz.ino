int read_ldr(){
  return (analogRead(LDR)*100)/1023;  
}
