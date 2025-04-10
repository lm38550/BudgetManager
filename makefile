# Nom de l'exécutable
TARGET = budget

# Fichiers sources
SRC = main.cpp

# wxWidgets compile & link flags
WX_CXXFLAGS = $(shell wx-config --cxxflags)
WX_LDFLAGS = $(shell wx-config --libs)

# Compilation
all:
	g++ $(WX_CXXFLAGS) -o $(TARGET) $(SRC) $(WX_LDFLAGS)

# Nettoyage
clean:
	rm -f $(TARGET)
