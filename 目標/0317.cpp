#include <iostream>
#include <fstream>

using namespace std;


int main(){
	
	const char *fileName = "0317.txt";
	
	ofstream ofs(fileName);
	
	if(!ofs){
		cout << "�t�@�C�����J���܂���ł����B\n";
		cin.get();
		return 0;
	}
	
	ofs << "�����������@����������" << endl;
	cout << fileName << "�ɏ������݂܂����B" << endl;


    cin.get();
	
	return 0;
}	

