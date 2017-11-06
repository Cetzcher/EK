
build:
	pip3 install pyinstaller
	pyinstaller --onefile --windowed main.py

clean:
	rm -r build
	rm -r dist

install:
	pip3 install pyqt5
	pip3 install websocket-client	

rebuild: clean build
