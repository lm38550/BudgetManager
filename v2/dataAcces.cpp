#include "dataAcces.h"
#include <unistd.h>
#include <vector>
#include <sqlite3.h>
#include <iostream>
#include <string>

using namespace std;

sqlite3* dataAcces::OpenDB() {
    sqlite3* db = nullptr;

    if (access(DB_PATH.c_str(), F_OK) == -1) {
        cerr << "Erreur : le chemin spécifié n'existe pas : " << DB_PATH << endl;
        return nullptr;
    }

    int rc = sqlite3_open(DB_PATH.c_str(), &db);

    if (rc != SQLITE_OK) {
        cerr << "Error on data base opening / Erreur lors de l'ouverture de la base de données : "
                    << sqlite3_errmsg(db) << endl;
        return nullptr;
    }

    cout << "Data base succefully opened / Base de données ouverte avec succès." << endl;
    return db;
}

void dataAcces::CloseDB(sqlite3* db) {
    if (db != nullptr) {
        sqlite3_close(db);
        cout << "Data base succefully closed / Base de données fermée avec succès.\n" << endl;
    }
}

vector<vector<string>> dataAcces::SearchInDB(sqlite3* db, const std::string& SQLrequest) {
    sqlite3_stmt* stmt = nullptr;
    vector<vector<string>> result;

    int rc = sqlite3_prepare_v2(db, SQLrequest.c_str(), -1, &stmt, nullptr);
    if (rc != SQLITE_OK) {
        std::cerr << "Erreur de préparation de la requête : "
                  << sqlite3_errmsg(db) << std::endl;
        return result;
    }

    // Boucle sur les lignes du résultat
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        int nbColonnes = sqlite3_column_count(stmt);
        vector<string> line;
        for (int i = 0; i < nbColonnes; ++i) {
            string valeur = reinterpret_cast<const char*>(sqlite3_column_text(stmt, i));
            line.push_back(valeur);
        }
        result.push_back(line);
        std::cout << std::endl;
    }

    sqlite3_finalize(stmt);
    return result;
}

bool dataAcces::ExecuteQuery(sqlite3* db, const std::string& SQLrequest) {
    char* errMsg = nullptr;
    int rc = sqlite3_exec(db, SQLrequest.c_str(), nullptr, nullptr, &errMsg);

    if (rc != SQLITE_OK) {
        std::cerr << "Erreur lors de l'exécution de la requête : "
                  << (errMsg ? errMsg : sqlite3_errmsg(db)) << std::endl;
        sqlite3_free(errMsg);
        return false;
    }

    std::cout << "Requête exécutée avec succès." << std::endl;
    return true;
}

string dataAcces::TestingDB() {
    sqlite3* db;
    db = OpenDB();
    if(db == nullptr) {
        return "Data base could not open on test";
    }
    CloseDB(db);
    return "Test on data base went well";
}

dataAcces::dataAcces() {
    cout << TestingDB() << endl;
}

// --------------------------------------------------------------------------------
// -------------------- Acces to all the content of each table --------------------
// --------------------------------------------------------------------------------

void dataAcces::getAccountList(vector<int> & IDacc, vector<string> & NameAcc, vector<float> & Balance)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT * FROM Accounts");
    CloseDB(db);

    IDacc.clear();
    NameAcc.clear();
    Balance.clear();
    for(int i = 0 ; i < data.size() ; i++) {
        IDacc.push_back(stoi(data[i][0]));
        NameAcc.push_back(data[i][1]);
        Balance.push_back(stof(data[i][2]));
    }
}

void dataAcces::getBudgetList(vector<int> & Year, vector<int> & Month, vector<int> & Cat, vector<float> & Amount, vector<float> & Used)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT * FROM Budget");
    CloseDB(db);

    Year.clear();
    Month.clear();
    Cat.clear();
    Amount.clear();
    Used.clear();
    for(int i = 0 ; i < data.size() ; i++) {
        Year.push_back(stoi(data[i][0]));
        Month.push_back(stoi(data[i][1]));
        Cat.push_back(stoi(data[i][2]));
        Amount.push_back(stof(data[i][3]));
        Used.push_back(stof(data[i][4]));
    }
}

void dataAcces::getCategoryList(vector<int> & IDcat, vector<string> & NameCat)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT * FROM Categories");
    CloseDB(db);

    IDcat.clear();
    NameCat.clear();
    for(int i = 0 ; i < data.size() ; i++) {
        IDcat.push_back(stoi(data[i][0]));
        NameCat.push_back(data[i][1]);
    }
}

void dataAcces::getHistoryList(vector<int> & IDope, vector<int> & Year, vector<int> & Month, vector<int> & Day, vector<int> & Acc, vector<int> & Cat, vector<float> & Amount, vector<string> & Comment)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT * FROM History");
    CloseDB(db);

    IDope.clear();
    Year.clear();
    Month.clear();
    Day.clear();
    Acc.clear();
    Cat.clear();
    Amount.clear();
    Comment.clear();
    for(int i = 0 ; i < data.size() ; i++) {
        IDope.push_back(stoi(data[i][0]));
        Year.push_back(stoi(data[i][1]));
        Month.push_back(stoi(data[i][2]));
        Day.push_back(stoi(data[i][3]));
        Acc.push_back(stoi(data[i][4]));
        Cat.push_back(stoi(data[i][5]));
        Amount.push_back(stof(data[i][6]));
        Comment.push_back(data[i][7]);
    }
}

// --------------------------------------------------------------------------------
// --------------------------- Acces to Account content ---------------------------
// --------------------------------------------------------------------------------

float dataAcces::getAccountBalanceByID(int ID)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT Balance FROM Accounts WHERE IDAccount = " + to_string(ID) + ";");
    CloseDB(db);

    return stof(data[0][0]);
}

string dataAcces::getAccountNameByID(int ID)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT Name FROM Accounts WHERE IDAccount = " + to_string(ID) + ";");
    CloseDB(db);

    return data[0][0];
}

int dataAcces::getAccountIDByName(string Name)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT IDaccount FROM Accounts WHERE Name = '" + Name + "';");
    CloseDB(db);

    return stoi(data[0][0]);
}

// --------------------------------------------------------------------------------
// ------------------------------ Set Account content -----------------------------
// --------------------------------------------------------------------------------

void dataAcces::CreateNewAccount(string Name)
{
    sqlite3* db;
    db = OpenDB();
    bool query = ExecuteQuery(db, "INSERT INTO Accounts (Name, Balance) VALUES ('" + Name + "', 0.00)");
    CloseDB(db);
}

// --------------------------------------------------------------------------------
// --------------------------- Acces to Budget content ----------------------------
// --------------------------------------------------------------------------------

void dataAcces::getBudgetByYMC(int Year, int Month, int Cat, float & Amount, float & Used) {
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT Amount, Used FROM Budget WHERE Year = " + to_string(Year) + " AND Month = " + to_string(Month) + " AND Category = " + to_string(Cat) + ";");
    CloseDB(db);

    Amount = stof(data[0][0]);
    Used = stof(data[0][1]);
}

// --------------------------------------------------------------------------------
// -------------------------- Acces to Category content ---------------------------
// --------------------------------------------------------------------------------

string dataAcces::getCategoryNameByID(int ID) {
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT name FROM Categories WHERE IDCategory = " + to_string(ID) + ";");
    CloseDB(db);

    return data[0][0];
}

int dataAcces::getCategoryIDByName(string Name) {
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT IDCategory FROM Categories WHERE name = '" + Name + "';");
    CloseDB(db);

    return stoi(data[0][0]);
}

// --------------------------------------------------------------------------------
// --------------------------- Acces to History content ---------------------------
// --------------------------------------------------------------------------------

void dataAcces::getHistoryByID(int ID, int & Year, int & Month, int & Day, int & Acc, int & Cat, float & Amount, string & Comment) {
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT * FROM History WHERE OperationID = " + to_string(ID) + ";");
    CloseDB(db);

    Year = stoi(data[0][1]);
    Month = stoi(data[0][2]);
    Day = stoi(data[0][3]);
    Acc = stoi(data[0][4]);
    Cat = stoi(data[0][5]);
    Amount = stof(data[0][6]);
    Comment = data[0][7];
}
