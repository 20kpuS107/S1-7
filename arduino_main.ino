const int heart_rate_sensor = A0;
unsigned long duration;

void setup(){
	Serial.begin(115200); //라즈베리파이와이 시리얼 시간맞추기
	pinMode( heart_rate_sensor, INPUT_PULLUP);
}
void loop(){
	duration = pulseIn(heart_rate_sensor, HIGH); //핀이 HIGH될때까지 기다림 심박있을경우
	float bpm_float = 60000/duration; // bpm 계산 mm단위
	int bpm = int(bpm_float); //소숫점버림
	Serial.println(bpm); //Serial통신으로 라즈베리파이에 bpm 수치 전달
}