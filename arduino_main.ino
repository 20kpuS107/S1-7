const int heart_rate_sensor = A0;
unsigned long duration;

void setup(){
	Serial.begin(115200); //��������̿��� �ø��� �ð����߱�
	pinMode( heart_rate_sensor, INPUT_PULLUP);
}
void loop(){
	duration = pulseIn(heart_rate_sensor, HIGH); //���� HIGH�ɶ����� ��ٸ� �ɹ��������
	float bpm_float = 60000/duration; // bpm ��� mm����
	int bpm = int(bpm_float); //�Ҽ�������
	Serial.println(bpm); //Serial������� ��������̿� bpm ��ġ ����
}