# Nom de l'exécutable
TARGET = target/budget

# Fichiers sources
SRC = src/main.cpp \
      src/models/dataAcces.cpp \
      src/pages/accounts_edit.cpp

# wxWidgets compile & link flags
WX_CXXFLAGS = $(shell wx-config --cxxflags)
WX_LDFLAGS = $(shell wx-config --libs)

# SQLite link flags
SQLITE_LDFLAGS = -lsqlite3

# Options de compilation
CXXFLAGS = -std=c++17 -Wall

# Compilation
all:
	@mkdir -p target
	g++ $(CXXFLAGS) $(WX_CXXFLAGS) -o $(TARGET) $(SRC) $(WX_LDFLAGS) $(SQLITE_LDFLAGS)

# Nettoyage
clean:
	rm -f $(TARGET)
