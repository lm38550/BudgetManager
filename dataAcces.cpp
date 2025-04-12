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
        cout << "Data base succefully closed / Base de données fermée avec succès." << endl;
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

    std::cout << "Résultats de la requête :\n";

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

void dataAcces::getAccountList(vector<int> & IDacc, vector<string> & NameAcc, vector<int> & Balance)
{
    cout << "NOT DEFINED YET" << endl;
}

void dataAcces::getBudgetList(vector<int> & Year,  vector<int> & Month, vector<int> & Cat, vector<float> & Amount, vector<float> & Used)
{
    cout << "NOT DEFINED YET" << endl;
}

void dataAcces::getCategoryList(vector<int> & IDcat, vector<string> & NameCat)
{
    sqlite3* db;
    db = OpenDB();
    vector<vector<string>> data = SearchInDB(db, "SELECT * FROM Categories");
    CloseDB(db);

    IDcat.clear();
    NameCat.clear();
    for(int i = 0 ; i < 4 ; i++) {
        IDcat.push_back(stoi(data[i][0]));
        NameCat.push_back(data[i][1]);
    }
}

void dataAcces::getHistoryList(vector<int> & IDope, vector<int> & Year, vector<int> & Month, vector<int> & Day, vector<int> & Acc, vector<int> & Cat, vector<float> & Amount, vector<string> & Comment)
{
    cout << "NOT DEFINED YET" << endl;
}