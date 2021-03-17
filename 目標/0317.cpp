#include <iostream>
#include <fstream>

using namespace std;


int main(){
	
	const char *fileName = "0317.txt";
	
	ofstream ofs(fileName);
	
	if(!ofs){
		cout << "ファイルが開けませんでした。\n";
		cin.get();
		return 0;
	}
	
	ofs << "あいうえお　かきくけこ" << endl;
	cout << fileName << "に書き込みました。" << endl;


    cin.get();
	
	return 0;
}	

