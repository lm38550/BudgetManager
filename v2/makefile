# Nom de l'exécutable
TARGET = budget

# Fichiers sources
SRC = main.cpp dataAcces.cpp pages/accounts_edit.cpp

# wxWidgets compile & link flags
WX_CXXFLAGS = $(shell wx-config --cxxflags)
WX_LDFLAGS = $(shell wx-config --libs)

# SQLite link flags
SQLITE_LDFLAGS = -lsqlite3

# Compilation
all:
	g++ $(WX_CXXFLAGS) -o $(TARGET) $(SRC) $(WX_LDFLAGS) $(SQLITE_LDFLAGS)

# Nettoyage
clean:
	rm -f $(TARGET)
